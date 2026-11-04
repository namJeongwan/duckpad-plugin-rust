# Duckpad Rust support 0.1.0

First independent release of the signed Rust language-provider package for Duckpad 0.17.0 (host API 1.5.0). Provides rust-analyzer through the common completion client, with per-workspace and folder server settings. Runtime/toolchain discovery uses the external project environment; there is no separate interpreter selector.

Server binaries and project dependencies remain external. Download `Duckpad-Rust-0.1.0.zip` and extract it, then select the extracted `.duckpad-plugin` folder with Install Plugin, or select this provider in Available Plugins after catalog publication.

The package signature, inventory and deterministic archive are verified before publication. The host implementation was tested with actual language servers on Apple Silicon. Intel hardware, macOS 13 runtime and a full Rails application were not exercised.
