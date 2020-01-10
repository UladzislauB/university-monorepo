using System;
using System.Threading.Tasks;
using MailKit.Net.Smtp;
using Microsoft.AspNetCore.Mvc;
using MimeKit;

namespace weblog.Controllers
{
    public class ContactController: Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}