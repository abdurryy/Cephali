var onloadCallback = function() {
    grecaptcha.render('captcha_holder', {
      'sitekey' : document.getElementById("site_key").innerHTML
    });
};