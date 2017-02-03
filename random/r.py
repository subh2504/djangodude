import hashlib

#c27ab93c2dfd5cd75b153504f765fd22f74e3ce3065a4e6f284dc0885b5d6b1a907c6c2e5e5afdbb71dc1bc88bbce84ca1554be2a9cd5adfcbe2295351c00cfd
def enc(str1):
    md = hashlib.sha1()
    print(str1.encode())
    md.update(str1.encode())
    return str(md.hexdigest())


#amount=50.00&statusmessage=The+payment+has+been+successfully+collected&checksum=f03d111b97e3d7b02e1bbb25194f1498fafde6f4fadd28c569adb18a234ff710&mid=MBK7518&orderid=6DtArudG2EIecD&statuscode=0

#print(enc("/L26wjbRzLKxSmXN9Zp9ilTrX3vxoRMdPILaq5ygLwt+ZdjUEpd2MQ=="+"1483113418162"+"SHRPAN2212VIK0312BHUPAR8762KLMBIJ87"))
print(enc("" + "1485615148483" + "SATPANYOG2212VIK0312BHUPAR8762VIKANUJ87"))
