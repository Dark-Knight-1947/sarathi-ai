# LLM - Application Launcher 

## 1. Goal

We want Sarathi to understand natural-language commands such as "Open Spotify" and actually perform that action on the computer. 

```text
User: "Open Spotify"
        ↓
LLM understands intent
        ↓
LLM calls open_application(name="spotify")
        ↓
Python executes the function
        ↓
Windows launches Spotify
```

## 2. Approach 0.1 - Hardcoded

We initially created:
```python
{
    "type": "function",
    "name": "open_spotify",
    "description": "Open Spotify on the computer."
}
```
and python handled it with:
```python
if item.name == "open_spotify":
    open_spotify()
```


## 3. Issues with Approach 0.1
 
 This is not scalable. 
 If we have 100 applications/tools/softwares, we'll need 100 if-else statements.

 Lesson: Give LLM the capability, not a seperate toold for every application


## 4. The generic open_application() tool

Our new tool is: open_application(name)

The LLM doesn't need to know how the application is launched. 
It only needs to know:
- Tool: open_application()
- Input: application name
- Purpose: Open an application installed on the computer 


## 5. How does python find applications?

This is where we built applications.py 

We use two sources:
A. Windows registered applications
--> Using:
    ```powershell
    Get-StartApps
    ```
--> This gives Windows' list of applications available through the Start Menu, including their: Name & AppID

B. .lnk shortcuts 
--> We also search the Start Menu shortcut locations: APPDATA & PROGRAMDATA 
--> & then find .lnk 


## 6. Why APPDATA and PROGRAMDATA?

A. APPDATA
--> Contains application data/configuration associated with the current user.
--> We use its Start Menu Programs directory to find shortcuts available to that user.

B. PROGRAMDATA 
--> Contains data shared across users.
--> We use its Start Menu Programs directory to find shortcuts available more broadly on the computer.

We aren't searching all of APPDATA or PROGRAMDATA. We specifically construct their Start Menu → Programs paths.


## 7. Getting Windows Application Data 

We had an issue where simply doing:
```python
subprocess.run(["powershell", ...])
```
didn't work because powershell.exe wasn't available through the PATH in our environment.

Thus, we used it's explicit path:
```python
powershell = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
```


## 8. Problem with parsing the normal PowerShell table?

Initially we tried:
```python
parts = line.split()

name = parts[0]
app_id = parts[1]
```
But this broke for application names containing multiple words (Ex: Visual Studio Code)

For example, an output like:
Visual Studio Code 4!235@341VSCODE 

could become: 
```python
["Visual", "Studio", "Code", "4!235@341VSCODE"]
```

and Python would incorrectly assume: 
```python
name = "Visual"
app_id = "Studio"
```


## 9. Solution

We changed/manipulated Powershell output to:
Name | AppId

using:
```python
Get-StartApps | ForEach-Object { "$($_.Name)|$($_.AppID)" }
```

Then, python can safely do:
```python
name, app_id = line.split("|", 1)
```

Lesson: Don't rely on parsing human-formatted tables. If possible, make the source produce structured predicatable output. 


## 10. Creating application dictionary 

We create:
```pyton
applications = {}
```

to create an application dictionary with key as App_name & value as App_ID


## 11. Launching Windows Registered applications 

We discovered that Windows can launch these applications through:
shell:AppsFolder\</AppID>

and Python does:
```python
os.startfile(f"shell:AppsFolder\\{app_id}")
```

Flow:
```text
AppID
 ↓
shell:AppsFolder\<AppID>
 ↓
Windows Shell
 ↓
Application launches
```


## 12. Open_Application() Logic 

```text
open_application(name)
        ↓
Check Windows registered applications
        ↓
Found?
 ├── YES → launch AppID
 │
 └── NO
       ↓
Check .lnk shortcuts
       ↓
     Found?
      ├── YES → launch shortcut
      │
      └── NO → return "I couldn't find..."
```


## 13. Connecting it to the LLM 

Our main.py gives the LLM this tool:
```python
{
    "type": "function",
    "name": "open_application",
    ...
}
```

The LLM sees the user's request and decides whether this tool is appropriate.

For:
Open Spotify 

the model generates a function call like:
```python
open_application(name="spotify")
```

The model isn't directly opening an application. Instead, it's requesting our Python Program to execute the tool.


## 14. Final Architecture

```text

                 USER
                   │
                   ▼
     "I want to hear music on Spotify"
                   │
                   ▼
              OpenAI LLM
                   │
                   │ function call
                   ▼
       open_application("spotify")
                   │
                   ▼
            applications.py
                   │
          ┌────────┴────────┐
          ▼                 ▼
 Windows registered      .lnk shortcuts
 applications
          │                 │
          ▼                 ▼
        AppID            .lnk path
          │                 │
          └────────┬────────┘
                   ▼
                WINDOWS
                   │
                   ▼
              APPLICATION
```


## 16. Milestone 

Milestone 1 — Sarathi can take action.

Sarathi is no longer limited to generating text. The LLM can understand a user's natural-language request, select an appropriate tool, pass arguments to Python, and cause an actual action to happen on the computer.