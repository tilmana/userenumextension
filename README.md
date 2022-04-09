# userenumextension
Kerbrute userenum results parsing utility

When getting output from Kerbrute's userenum module, you will often find duplicates (atleast in my CTF experience) of users. Because Active Directory is not case-sensitive, this makes it take time to figure out from the output the unique users. This script takes in the output file from Kerbrute's userenum (or any text file that contains it) and will return unique users. This script is especially useful when working with the output file of large enterprise networks, where many users and their duplicates will be present in the output.

usage: python3 userparse.py {file.txt}

![image1](https://user-images.githubusercontent.com/59236083/162578583-152f2015-9349-482e-9dc1-d71be519bc4d.png)

![image2](https://user-images.githubusercontent.com/59236083/162578584-2fc2640b-dd2a-42e9-af1a-96836c43bdc4.png)
