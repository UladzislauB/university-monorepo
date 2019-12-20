using System;
using System.Threading.Tasks;
using MailKit.Net.Smtp;
using Microsoft.AspNetCore.Mvc;
using MimeKit;

namespace weblog.Controllers
{
    public class ContactController: Controller
    {
        public async Task SendEmail()
        {
            var emailMessage = new MimeMessage();
 
            emailMessage.From.Add(new MailboxAddress("Администрация сайта", "vladislausdeminov@yandex.ru"));
            emailMessage.To.Add(new MailboxAddress("", "vasilyuk.vlad.kbr@yandex.ru"));
            emailMessage.Subject = "ASP.net weblog";
            emailMessage.Body = new TextPart();
            
            using (var client = new SmtpClient())
            {
                client.ConnectAsync("smtp.yandex.ru", 25, false);
                client.AuthenticateAsync("vladislausdeminov@yandex.ru", "XCc4ahcdfK6WMB2");
                client.SendAsync(emailMessage);
 
                client.DisconnectAsync(true);
            }
        }

        public async Task<IActionResult> SendMessage()
        {
            await SendEmail();
            return RedirectToAction("Index");
        }

        public IActionResult Index()
        {
            return View();
        }
    }
}