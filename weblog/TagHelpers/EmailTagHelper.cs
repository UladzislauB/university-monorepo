using MailKit.Net.Smtp;
using Microsoft.AspNetCore.Razor.TagHelpers;
using MimeKit;

namespace weblog.TagHelpers
{
    public class EmailTagHelper : TagHelper
    {
        public string Address { get; set; }
        public string Content { get; set; }

        public override void Process(TagHelperContext context, TagHelperOutput output)
        {
            output.TagName = "a";
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
            
            output.Attributes.SetAttribute("href", "#");
            output.Content.SetContent(Content);
        }
    }
}