import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")

def sendEmail():
  Msg = outlook.CreateItem(0) # Email
  Msg.To = "test@test.com" # you can add multiple emails with the ; as delimiter. E.g. test@test.com; test2@test.com;
  Msg.CC = "test@test.com"
  Msg.Subject = "Subject"
  Msg.Body = "Your text (not html)"
  Msg.Send()
def sendMeeting():    
  appt = outlook.CreateItem(1) # AppointmentItem
  appt.Start = "2022-01-10 2:40" # yyyy-MM-dd hh:mm
  appt.Subject = "Test subject"
  appt.Duration = 30 # In minutes (60 Minutes)
  appt.Location = "Location Name"
  appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added
  
  appt.Recipients.Add("dhimes@gmail.com") # Don't end ; as delimiter

  appt.Save()
  appt.Send()

sendMeeting()