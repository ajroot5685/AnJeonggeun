{
  description = "sudosubin/pirogramming-19th-deployment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs { inherit system; config.allowUnsupportedSystem = true; };

        in
        {
          devShell = pkgs.mkShell rec {
            venvDir = "./.venv";

            buildInputs = with pkgs; [
              python311
              python311Packages.venvShellHook
            ];
          };
        }
      );
}
