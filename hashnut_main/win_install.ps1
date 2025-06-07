$targetDir = "$env:USERPROFILE\bin"
$batFileName = "hashnut.bat"
$sourceBatPath = ".\$batFileName"

if (-Not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir
    Write-Host "Created directory $targetDir"
}

Copy-Item -Path $sourceBatPath -Destination "$targetDir\$batFileName" -Force
Write-Host "Copied $batFileName to $targetDir"


$envPath = [Environment]::GetEnvironmentVariable("PATH", "User")

if ($envPath -notlike "*$targetDir*") {
    $newPath = "$envPath;$targetDir"
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "Added $targetDir to User PATH environment variable"
} else {
    Write-Host "$targetDir is already in User PATH"
}

Write-Host "Installation complete! Please restart your terminal or log off/on to apply PATH changes."

