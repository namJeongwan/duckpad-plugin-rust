# Duckpad Rust support

Optional, independently installed language-provider plugin. Version **0.1.0** requires Duckpad **0.17.0 or later** with host API 1.5.0 (below 2.0.0).

Install through Plugins Admin → Available Plugins, or download the release ZIP and choose Install Plugin. Then install rust-analyzer and your project dependencies separately. Server binaries are not included or downloaded automatically. Choose server settings under Preferences → Language Support; overrides belong to the current workspace or selected folder. Runtime/toolchain discovery uses the external project environment; this provider does not expose a separate interpreter selector.

This declarative package registers signed launch definitions with Duckpad's common LSP client. No native library, WASM module or language server binary is shipped. Servers execute through Duckpad's existing unsandboxed helper. Disable or uninstall the plugin to withdraw its registrations; project files and environments are retained.

## Build and verify

On macOS with Swift and Python 3 installed, run `python3 scripts/package.py`. It verifies the existing signed manifest with the public key and creates `dist/Duckpad-Rust-0.1.0.zip`. The private publisher key is not stored here; editing the signed definition requires the maintainer to issue a newly signed package.

Source definitions originate from [Duckpad's language-provider implementation](https://github.com/namJeongwan/duckpad/tree/bdf63dd7dd79d833f5193763308a640ab3212a8a/LanguagePlugins). See the [language plugin SDK](https://github.com/namJeongwan/duckpad/blob/bdf63dd7dd79d833f5193763308a640ab3212a8a/SDK/LanguageSupport/language-support.md) for the contract.
