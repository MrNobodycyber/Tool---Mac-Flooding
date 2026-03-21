# Tool---Mac-Flooding

 Hey !
 I'm creating a web penetration security tool.

 In this part, you will find all the version and improvements of my program as i update it !

This is a to ol of pentesting that i'm creating. The purpose is to use of a vulnerability called "Mac Flooding", which involves overflowing the switch’s memory area used to store source MAC addresses.

This tool isn’t complete yet; it’s currently under development.

Hope you enjoy it !


-----------------------------------------------------------------------------------------------

2ND VERSION : UPDATES

-----------------------------------------------------------------------------------------------

1 .Usage of a condition if the dictionnary of MAC address is empty; in verify function.

2 .Replace the type of the var dict with {} and not [].

3. The while loop " while i<len(dict_al) -1 :" replaced by " while i<len(dict_al) :" to avoid out of range error.

4. Bad utilisation of the native Scapy function "rand_MAC" -> "randMAC"

5. The frame that was sent contained the same sources and destination MAC address with the usage of the var "rd_MAC" -> just changed Ether(dst= rd_MAC, type=0x0800) / IP(dst='255.255.255.255')" and suppress the src option.

6. Usage of "raise " to initiate an error if the frame is in the known MAC dictionnary; with an "ValueError" error.

7. Raise will be used with the "try" in line
