# Docker

## Visual Studio Code

<details>
    <summary>Settings for Visual Studio Code</summary>
    <p>
    <ul>
    <li><a href="https://code.visualstudio.com/docs/containers/reference#_command-customization">VSCode Docs</a></li>
    </ul>
    </p>

#### Use the following in your .vscode/settings.json

```json
{
  "docker.commands.composeDown": [
    {
      "label": "Docker: Compose Down",
      "template": "docker-compose ${configurationFile} down --remove-orphans"
    }
  ]
}
```

</details>

## IntelliJ
