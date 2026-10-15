# Voice Studio VN-EN — starter

A Windows desktop starter project for a Vietnamese/English voice-cloning application.

## What this starter does now
- Provides a PySide6 desktop GUI.
- Lets you select a reference audio file and enter text.
- Includes language and engine-mode selectors (offline / online).
- Includes a GitHub Actions workflow that builds a Windows setup installer on a hosted Windows runner.
- Does **not yet clone voices**: the inference adapter is intentionally a stub until a specific model/provider is selected and tested.

## No local Python installation required
Use GitHub Codespaces to edit/run the Python GUI remotely, and GitHub Actions to build the Windows artifact. The `.exe` build happens on GitHub's Windows runner.

## 1. Create a GitHub repository
1. Sign in at https://github.com/
2. Create a new repository named `voice-studio-vn-en`.
3. Upload these files (or upload this ZIP's contents) to the repository root.
4. For the easiest free build workflow, choose a **public** repository. Public repositories use standard GitHub-hosted Actions runners free of charge; private repositories have plan quotas.

## 2. Open Codespaces
1. Open your repository on GitHub.
2. Click **Code** → **Codespaces** → **Create codespace on main**.
3. Wait for the browser VS Code editor to open.
4. In the integrated terminal run:
   ```bash
   python --version
   pip install -r requirements.txt
   python -m app.main
   ```
The terminal and Python runtime are in the cloud Codespace, not installed on your PC.

## 3. Build a Windows EXE
1. Commit and push the files to the `main` branch.
2. Open the repository's **Actions** tab.
3. Select **Build Windows app**.
4. Click **Run workflow** (or push a commit to trigger it).
5. Wait for the workflow to finish successfully.
6. Open the completed workflow run and download the `VoiceStudio-Windows` artifact.
7. Extract the ZIP on your Windows PC and run `VoiceStudio.exe`.

The first build may take several minutes. The artifact is a Windows setup installer (`VoiceStudio-VN-EN-Setup.exe`). It is unsigned, so Windows SmartScreen may show a warning. Validate it before distributing it.

## 4. Voice model integration (next stage)
This starter does not include model weights or an inference engine. Before implementing generation, choose a model/provider that supports both Vietnamese and English and review:
- model license and commercial-use restrictions,
- supported languages and quality,
- GPU/CPU requirements,
- redistribution terms for model weights,
- online provider pricing, API limits and privacy policy.

The app should only clone your own voice or a voice you have explicit permission to use.

## Troubleshooting
- If the workflow cannot find an icon/resource, check `app/main.py` and `voice_studio.spec`.
- If the EXE opens and immediately closes, run it from Command Prompt to inspect the error, or use the workflow logs.
- Large AI models should not be bundled into a first prototype. Build the GUI first, then add and test the model adapter.
