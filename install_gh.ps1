$url = (Invoke-RestMethod -Uri 'https://api.github.com/repos/cli/cli/releases/latest').assets | Where-Object { $_.name -like '*windows_amd64.msi' } | Select-Object -ExpandProperty browser_download_url
Invoke-WebRequest -Uri $url -OutFile 'gh.msi'
Start-Process msiexec.exe -ArgumentList '/i gh.msi /quiet' -Wait
Remove-Item 'gh.msi'
