from airflow.utils.log.secrets_masker import SecretsMasker

filt = SecretsMasker()
# filt.add_mask('password')

key = "env"
dict1 = ({'api_key': 'masked based on key name', 'other': 'foo'},)
dict2 = ({'api_key': '***', 'other': 'foo'},)
print(filt.redact(dict1, "env"))

value = """
Running command BlackHole: sh -c "set -o pipefail && sudo /tmp/mysql/xtrabackup/8.0-linux-x86_64/xtrabackup --defaults-file=/db2/etc/my.cnf --host=192.168.77.203 --incremental --incremental-lsn=331703726 --connect_timeout=10 --safe-slave-backup --slave_info --user='dbagent' --port=5501 --password='1qaz@WSX' --datadir=/db2/data/data/ --parallel=6 --backup --stream=xbstream | lz4 -B4 | ssh -c aes256-gcm@openssh.com -p 22 root@192.168.90.44 'lz4 -d -B4 | sudo xbstream -x -C /root/mysql_backup'"
"""
print(filt.redact(value, None))
