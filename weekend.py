from splinter import Browser

browser = Browser() # defaults to firefox
browser.visit('https://industry.socs.binus.ac.id/learning-plan/auth/login')
#login
browser.fill('username','2001542153')
browser.fill('password','24081998')
browser.find_by_value('Login').click()

#log-book
browser.visit('https://industry.socs.binus.ac.id/learning-plan/student/log-book')
browser.fill('clock-in','09.00')
browser.fill('clock-out','18.00')
browser.fill('activity','Off')
browser.fill('description','Off')
browser.find_by_text('Submit').click()

print("sudah selesai pak")

browser.quit()
