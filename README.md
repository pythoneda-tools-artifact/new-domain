# new-domain

Tool to create new PythonEDA domains.

## Usage

To run this tool, check the latest tag of the [https://github.com/pythoneda-tools-artifact-def/new-domain](definition repository):

``` sh
nix run https://github.com/pythoneda-tools-artifact-def/new-domain/[version] [-h|--help] [-n|--namespace namespace] [-t|--github-token githubToken] [-g|--gpg-key-id gpgKeyId]
```
- `-h|--help`: Prints the usage.
- `-n|--namespace`: The Python namespace, for example `pythoneda.my_domain`
- `-t|--github-token`: The github token.
- `-g|--gpg-key-id`: The GnuPG key id.
