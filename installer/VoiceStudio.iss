#define MyAppName "Voice Studio VN-EN"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Voice Studio VN-EN"

[Setup]
AppId={{1F0A6B9C-93F8-49B0-9A58-2E36F91D2D81}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\VoiceStudioVNEN
DefaultGroupName={#MyAppName}
OutputDir=..\installer-output
OutputBaseFilename=VoiceStudio-VN-EN-Setup
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=lowest
WizardStyle=modern
Compression=lzma2
SolidCompression=yes
Uninstallable=yes

[Files]
Source: "..\dist\VoiceStudio\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Voice Studio VN-EN"; Filename: "{app}\VoiceStudio.exe"
Name: "{autodesktop}\Voice Studio VN-EN"; Filename: "{app}\VoiceStudio.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Run]
Filename: "{app}\VoiceStudio.exe"; Description: "Launch Voice Studio VN-EN"; Flags: postinstall nowait skipifsilent
