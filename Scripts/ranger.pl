#!/usr/bin/perl
use Digest::MD5 qw(md5 md5_hex md5_base64);
use IO::Select;
use HTTP::Response;
use HTTP::Request::Common qw(GET);
use URI::URL;
use IO::Socket::INET;
use Term::ANSIColor qw(:constants);
use MIME::Base64;
use LWP;
use HTTP::Cookies;
use HTML::Entities;
use URI::Escape;
use Win32::Console::ANSI;
use Term::ANSIColor;
use LWP::UserAgent;
use HTTP::Request;
use HTTP::Request::Common qw(POST);
use LWP::UserAgent;
use HTTP::Request::Common;
use Term::ANSIColor;
use HTTP::Request::Common qw(GET);
$ag = LWP::UserAgent->new();
use MIME::Base64;
use WWW::Mechanize;
use threads;
system("title Ip Ranger Null");
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }    print color('reset');
print color('red');
$logo="


  ___ ____    ____      _    _   _  ____ _____ ____  
 |_ _|  _ \  |  _ \    / \  | \ | |/ ___| ____|  _ \ 
  | || |_) | | |_) |  / _ \ |  \| | |  _|  _| | |_) |
  | ||  __/  |  _ <  / ___ \| |\  | |_| | |___|  _ < 
 |___|_|     |_| \_\/_/   \_\_| \_|\____|_____|_| \_\
                                                     

";
print $logo;
print "\n";
print colored ("                          Type: Ip Range \n",'green');
print colored ("                          Author: Null\n",'cyan');
print color 'reset';
print color("green"), "\n";
print color("green"),"./Select: \n";
print color("green"), "\n";
print color 'reset';
print color("cyan"), "Enter IP List :";
my $list=<STDIN>;
chomp($list);
	open (THETARGET, "<$list") || die "[-] Can't open the List of site file ?!";
@TARGETS = <THETARGET>;
close THETARGET;
$link=$#TARGETS + 1;
OUTER: foreach $tofuck(@TARGETS){
chomp($tofuck);
if($tofuck =~ /http:\/\/(.*)\//) {
$tofuck= $1;
gett();
}else{
gett();
}

}


##############################
sub gett(){
$ip= (gethostbyname($tofuck))[4];
my ($a,$b,$c,$d) = unpack('C4',$ip);
for ($i = 1; $i <= 255; $i+=1){
$ips ="$a.$b.$c.$i";
OUTER: foreach $ip($ips){
print color('bold red')," Ping : $ips\n";
        print TEXT "$ips\n";
        close (TEXT);
				open(save, '>>Ips.txt');
    print save "$ips\n";
    close(save);
$dork="ip:$ips";
}
}
}
#############################
sub get(){

$ip= (gethostbyname($tofuck))[4];
my ($a,$b,$c,$d) = unpack('C4',$ip);
$ips="$a.$b.$c.$d";
print color('bold green')," IP : $ips\n";
        print TEXT "$ips\n";
        close (TEXT);
		open(save, '>>ipranger.txt');
    print save "$ips\n";
    close(save);

$dork="ip:$ips";
}
####################################"