<#
  Exporta láminas de 1080x1350 desde un HTML de Plogy con Edge en modo headless.

  Uso (PowerShell, desde cualquier carpeta):
    .\render-slides.ps1 -Html "C:\ruta\pieza\cta-variantes.html" -OutDir "C:\ruta\pieza\exports\cta" -Param v -Keys b,c,d -Prefix cta-
    .\render-slides.ps1 -Html "C:\ruta\pieza\carrusel.html"      -OutDir "C:\ruta\pieza\exports"     -Param s -Keys 1,2,3,4,5,6 -Prefix slide-0

  El HTML muestra una sola lámina cuando recibe ?<Param>=<clave> (ver el script al final de los HTML de la pieza 001).
  Salida: <OutDir>\<Prefix><clave>.png

  Notas aprendidas:
  - Usar Start-Process -Wait desde PowerShell. Lanzar Edge en bucle desde bash dio salidas inconsistentes.
  - --virtual-time-budget=8000 da tiempo a que cargue Google Fonts (Space Grotesk). Sin red, cae a Helvetica/Arial y el layout cambia.
  - Edge imprime un error "fallback_task_provider" inofensivo; el PNG se escribe igual.
  - Verificar siempre el PNG a ojo (Read de la imagen) antes de darlo por bueno.
#>
param(
  [Parameter(Mandatory)] [string]$Html,
  [Parameter(Mandatory)] [string]$OutDir,
  [Parameter(Mandatory)] [string[]]$Keys,
  [string]$Param = "s",
  [string]$Prefix = "slide-",
  [int]$Width = 1080,
  [int]$Height = 1350,
  [string]$Edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
)

if (-not (Test-Path $Edge)) { throw "No encuentro Edge en $Edge" }
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$base = "file:///" + (($Html -replace '\\','/') -replace ' ','%20')

foreach ($k in $Keys) {
  $out = Join-Path $OutDir "$Prefix$k.png"
  $url = "$base`?$Param=$k"
  Start-Process -FilePath $Edge -ArgumentList @(
    "--headless=new","--disable-gpu","--hide-scrollbars",
    "--window-size=$Width,$Height","--virtual-time-budget=8000",
    "--screenshot=`"$out`"", $url
  ) -Wait -NoNewWindow 2>$null | Out-Null
  if (Test-Path $out) { Write-Output "ok  $out" } else { Write-Output "FALLO  $out" }
}
