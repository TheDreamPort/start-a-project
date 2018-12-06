# Silent Install Chrome
# https://enterprise.google.com/chrome/chrome-browser/

# Path for the workdir
$workdir = "c:\installer"

# Check if work directory exists if not create it

If (Test-Path -Path $workdir -PathType Container)
{ Write-Host "$workdir already exists" -ForegroundColor Red}
ELSE
{ New-Item -Path $workdir  -ItemType directory }

# Download the installer

$source = "https://dl.google.com/edgedl/chrome/install/GoogleChromeStandaloneEnterprise64.msi"
$destination = "$workdir\chrome.msi"

# Check if Invoke-Webrequest exists otherwise execute WebClient

if (Get-Command 'Invoke-Webrequest')
{
     Invoke-WebRequest $source -OutFile $destination
}
else
{
    $WebClient = New-Object System.Net.WebClient
    $webclient.DownloadFile($source, $destination)
}

# Start the installation

msiexec.exe /i "$workdir\chrome.msi" /q /norestart 

# Wait XX Seconds for the installation to finish

Start-Sleep -s 180

# Remove the installer

[System.Windows.MessageBox]::Show('Chrome Installation has completed!');
rm -Force $workdir\chrome*