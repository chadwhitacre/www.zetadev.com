#!/usr/local/bin/python
# what a hack :-)

import datetime

todays_date = datetime.date.today()
todays_date = todays_date.strftime('%B %d, %Y').replace(' 0', ' ')

print "Content-type: text/html"
print """
<html>
<head>

<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-247427-2";
urchinTracker();
</script>
    <title>Zeta Design & Development</title>
    <script type="text/javascript">
        /* FOUC thwart -- http://www.bluerobot.com/web/css/fouc.asp */
    </script>

    <style>@import url("/style.css");</style>
</head>
<body>
<div id="breadcrumbs">

    <div class="for-spacing">&nbsp;</div>



</div>
<div id="content-wrapper"><div class="padding">

    <a href="/" id="logo"><img src="/images/logo.png"
                               alt=""
                               title=""
                               height="93"
                               width="150" /></a>

    <div id="contact-info">
        1001 Merchant St, Ste 103<br />
        Ambridge, PA 15003-2381<br />

        www.zetaweb.com<br />
    </div>



    <div id="content">

        <h1></h1>

        <div>

    <div>%(date)s</div>

    <p>Dear Sir or Madam:</p>

    <p>Greetings! My name is Chad Whitacre. I am a partner in Zeta Design &
    Development, LLC, a software company. If you are not a system administrator
    or software developer yourself then you may be more interested in <a
    href="http://www.zetaweb.com">Zeta's retail website</a>.</p>

    <p>The purpose of this website is to share with you some of <a
    href="/software">the free software that I've developed</a>, and <a
    href="/misc">some miscellaneous articles that I've written</a>. I hope you
    find this material useful, and I look forward to your feedback.</p>

    <p>Thanks for stopping by!</p>

    <p>&nbsp;</p>

    <p>Yours truly,</p>

    <img src="/images/signature.png"
         alt="Chad W. L. Whitacre"
         title="Chad's signature"
         style="border: none;
                display: block;
                margin: 1em 1em 1em 0;" />

    <p>Chad W. L. Whitacre,<br />
       Partner, Zeta Design & Development<br />
       <a href="mailto:chad@zetaweb.com">
        chad@zetaweb.com
       </a>
    </p>

</div>

    </div>

</div></div>
</body>
</html>
""" % {'date':todays_date}
