
$invoc = Split-Path -Path $($MyInvocation.MyCommand.Path) -Parent

& pnputil /add-driver "$invoc/*.inf" /subdirs /install
