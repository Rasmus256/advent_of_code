('God{0}, Team Udland :)' -f $(If ($Hour -lt 12 ) { 'morgen' } Else { ' eftermiddag' })) | Write-Host -ForegroundColor Magenta

Write-Host("Hvor tit skal der skiftes tab?")
$interval = $null;
while($interval -eq $null) {
    $intervalString = Read-Host;
    $interval = $intervalString -as [int]
    if($interval -eq $null -or $interval -lt 1)
    {
        Write-Host("Ugyldig input - skal være et tal større end eller lig 1!")
    }
}

Write-Host("Skal browseren refreshes efter tab skifte? [y/j] for ja - alt andet for nej")
$refreshOnSwitch = $null;
while($refreshOnSwitch -eq $null)  {
    $refreshString = Read-Host;
    $refreshOnSwitch = $refreshString -match 'y.*' -or $refreshString -match 'j.*'
}

function LaunchGrafanaBrowser {
    start microsoft-edge:"https://grafana.fmt.bdpnet.dk/d/da5fb843-e494-4196-ba5a-44ebcbec1f5d/korer-kort-transaktioner-clearing?orgId=5&refresh=5s&from=-&to=now"
    start microsoft-edge:"https://grafana.fmt.bdpnet.dk/d/3wUiFdo4k/korer-betalingsflowet?orgId=5&refresh=5s&from=-&to=now"
}

Write-Host("Ok! Starter tab skifte om 5 sekunder, og hvert $interval sekund. Vil{0} udføre et tab refresh efter hvert skifte" -f $(if($refreshOnSwitch) {""} else {" IKKE"}))
Sleep 5;
$idx = 0;
while($true){
	$wshell=New-Object -ComObject wscript.shell; 
    Sleep 0.5; 
	if(!$wshell.AppActivate('Edge')) {
        Write-Host("Edge browser was not detected! Attempting to launch an Edge browser!")
        LaunchGrafanaBrowser
    } else {
        $wshell.SendKeys('^{PGUP}'); # Ctrl + Page Up keyboard shortcut to switch tab
        if($refreshOnSwitch) {
            $wshell.SendKeys('{F5}'); # F5 to refresh active page
        }
    }
    $idx = ($idx+1) % 25;
    Write-Progress -Activity "Tabswitcher" -PercentComplete ($idx * 4)
    Sleep $interval; 
}