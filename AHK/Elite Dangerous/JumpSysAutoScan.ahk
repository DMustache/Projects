XButton1::
Loop 1
SetKeyDelay, 100, 50
{
    Send, {Z}{0}
    {
        Send, {RButton down}
        Sleep, 8000
        Send, {RButton up}
    }
    Sleep, 10000
    Send, {X}
}exit