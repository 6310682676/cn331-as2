# CN331: WEB APP For enrollment
### Member
1. Parames Raikhao 6310680258
1. Suteekran Kangkreethaphol 6310682676

### Install Requirement
```
pip install -r requirement.txt
```

### Start Server
```
./manage.py runserver
```

### Role
1. Admin
2. User
   
### Admin
Login with username: admin, password: 123456 to login as admin
- Edit, Add subject

### Student
Login with username: 6310682676 password: 123456tu
- Enroll course
- Cancel course
- Check it detail by clicking a course code in the table

### How to use
There are 2 roles loging in for using. Enter your username and password as you are then sign in.

![DevOps](https://media.discordapp.net/attachments/770324554459250690/1020606880864813108/1663402016994.jpg)

------------------------------
### for student
- If you are loging-in as student following this direction. 

1.After you have registed as student, you will reach the home page and your name and username would be there. 4 bar icon links will offer you to go to the page that you want, there are enrollment-page mycourse-page courselist-page (these three pages contain your name lastname and username on the top) and log-out.

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020616694206570566/1663404301170.jpg)

2.If you click on enrollment-page link it will show you the enrollment-page. In this page you can enroll the courses that you want by clicking on the button enroll in each row if the button is green. The details will show you in the table also the status of the courses. If you need more information about the course you can click on the course code.

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020615306290409493/1663403742545.jpg)

3.If you click on courselist-page link it will show you the courselist-page. In this page it only shows you datail of each course also the status. If you need more information about the course you can click on the course code.

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020615306558832660/1663403742449.jpg)

4.If you click on mycourse-page link it will show you the mycourse-page. In this page you can see the list of courses that you have enrolled and also the detail of it. If you want to withdraw the course that you don't want you can click on the cancle-button in the end of each row to withdraw it. (In this process the course that you have cancled will be back to the enrollment-page) If you need more information about the course you can click on the course code.

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020615306961489990/1663403742349.jpg)

5.On the top of each page, it is Navbar that contains link-buttons that will bring you to the page that you want, there are Homepage-link enrollment-link mycourse-link courselist-link ang logout.

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020632693546954892/1663408155613.jpg)



------------------------------

### for admin
- If you are loging-in as admin following this direction. 

1.After you have registed as admin, the admin-page will appear. In this page you can edit all the details that you want by clicking on the edit-button in the end of each row and it will link you to the django admin browser in that course. But if you want to create new courses you can click on the add-button below to link to add django browser. 

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020616693925543936/1663404364113.jpg)

2.this is django browser. You can edit and add course by all the functions that show in this. 
![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020616693556461618/1663404374081.jpg)

3.On the top of each page, it is Navbar that contains link-buttons that will bring you to the page that you want, there are Homepage-link enrollment-link mycourse-link courselist-link ang logout.

![DevOps](https://cdn.discordapp.com/attachments/770324554459250690/1020632693546954892/1663408155613.jpg)

--------------------
