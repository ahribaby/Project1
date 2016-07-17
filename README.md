# Project1

Hello, I'm quite the beginner at Python but I like this language and am trying to create an anonymous email chat system. :)
So I've already got the code-behind for the website, but the email/database side is not quite set up. So I'm the system administrator (duh) for this and I've created a Gmail account solely for this project's purpose which I'm using as the admnistrator email address.

What this project will do is when a new user signs up, he will be assigned to a random group, and there will be an automated welcome email telling the user his random generated nickname and nicknames of other users in his group.

The .py file, test_email_1, is supposed to be this separate script where the email inbox is regularly processed to retrieve new emails. This script will also allow a user to send messages to all group members by setting the first line of the email message as "To: ALL". He can also send it to specific members of the group by setting it to "To: girl129, boy7786, rainy1037" (for example).

Also, if a user wishes to stop using this service, all he has to do is type out an email with the word "Unsubscribe" in the subject and send it to the administrator email address.
