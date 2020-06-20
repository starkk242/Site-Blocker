# Site-Blocker
Script to Block any site.

This script will block the selected sites to be accessed on the network.
The sites can be edited in the py file and can be edited there.

Review the below steps to schedule the script.

If you want to run the script in windows just open the start.bat file with adminstrator privalages(Right Click the file and select RUN AS ADMINISTRATOR).



#Scheduling in Windows: 

Scheduling of above script is little bit trick but I will guide you step by step-

First of all change the extension of your script from “.py” to “.pyw”.
Now open task scheduler.

Follow further instruction of scheduling carefully in order to schedule website blocker in your computer.

Click on “create task”. Fill the name of your choice and flag “Run with highest privilege”.

Now go to triggers, select “At startup” for begin the task.

Go to Action bar and create a new action and give path of your script.

Go to conditions bar and unflag the power section.

Press ok and you can see the script scheduled.

Finally restart your computer and see the magic.

Note: You can also check instantly by clicking run button.




#Scheduling above script in Mac : 

For scheduling above script in Mac you have to open crontab in your terminal as a root.

Write following command in terminal:
sudo crontab -e

Now press “i” to go into insert/editing mode and write @reboot python_script_path .

Save the tab by pressing first esc to quit write mode and fall back to command mode and now write “:wq” and finally press enter to validate.

Restart your system and see the magic.
