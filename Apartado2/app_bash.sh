get_mac() {
    OS=$(uname)
    case "$OS" in
        # Linux/macOS
        Linux*|Darwin*)
            if command -v ip >/dev/null 2>&1; then
                ip link show | awk '/link\/ether/ {print $2; exit}'
            elif command -v ifconfig >/dev/null 2>&1; then
                ifconfig | awk '/ether/ {print $2; exit} /HWaddr/ {print $5; exit}'
            else
                echo "MAC_DESCONOCIDA"
            fi
            ;;
        # Windows
        MINGW*|MSYS*|CYGWIN*)
            if command -v powershell >/dev/null 2>&1; then
                powershell -Command "(Get-NetAdapter | Where-Object Status -eq 'Up' | Select-Object -First 1).MacAddress" | tr -d '\r'
            else
                echo "MAC_DESCONOCIDA"
            fi
            ;;
        *)
            echo "MAC_DESCONOCIDA"
            ;;
    esac
}

MAC=$(get_mac)
OS=$(uname -s)
HOST=$(hostname)
USER_NOW=$(whoami)

echo "MAC=${MAC} | OS='${OS}' | HOST='${HOST}' | USER='${USER_NOW}'"