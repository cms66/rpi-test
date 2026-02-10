# Bash functions

test_func()
{
	read -p "test_func in func.sh"
}

show_vars()
{
	printf "var from vars.sh called from func.sh = $datadir\n"
}
