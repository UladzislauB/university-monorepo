using System;
using System.Threading.Tasks;
using MailKit.Net.Smtp;
using Microsoft.Extensions.Configuration;
using MimeKit;

namespace weblog.Services
{
    public class EmailService: IEmailService
    {
        private readonly IConfiguration Configuration;

        public EmailService(IConfiguration configuration)
        {
            Configuration = configuration;
        }
        public async Task SendEmailAsync(string email, string subject, string message)
        {
            var emailMessage = new MimeMessage();
 
            emailMessage.From.Add(new MailboxAddress("Администрация сайта", Configuration.GetSection("Smtp")["email"]));
            emailMessage.To.Add(new MailboxAddress("I", email));
            emailMessage.Subject = subject;
            emailMessage.Body = new TextPart(MimeKit.Text.TextFormat.Html)
            {
                Text = message
            };

            using (var client = new SmtpClient())
            {
                var host = Configuration.GetSection("Smtp")["name"];
                await client.ConnectAsync(host:host, 25, false);
                await client.AuthenticateAsync(Configuration.GetSection("Smtp")["email"], Configuration.GetSection("Smtp")["pwd"]);
                await client.SendAsync(emailMessage);
 
                await client.DisconnectAsync(true);
            }
        }
    }
}