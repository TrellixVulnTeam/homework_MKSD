软件名称：ftp开发

软件功能：
	1. 用户加密认证
    2. 多用户同时登陆
    3. 每个用户有自己的家目录且只能访问自己的家目录
    4. 对用户进行磁盘配额、不同用户配额可不同
    5. 用户可以登陆server后，可切换目录
    6. 查看当前目录下文件
    7. 上传下载文件，保证文件一致性
    8. 传输过程中现实进度条
    9. 支持断点续传

软件运行方法：
	1.配置bin目录下的ftp——server.py 或ftp_client.py 中ip 地址和端口，默认本地
	2.服务器端数据文件初始化：运行主目录下的setup.py
	3.服务器端管理用户数据：运行conf 目录下的root.py（待完善）
	4运行bin目录下的文件ftp——server.py 或ftp_client.py

软件使用说明：
	1.初始用户Calvin，密码123456，空间限额1G
	2.操作命令：
		upload 文件路径          上传文件至当前目录         
		download 文件名          下载文件至本地db目录下
		cd . 					 返回上层目录         
		cd 文件名 				 切换目录
		pwd      				 显示当前目录
		ls                       显示当前目录所有文件
		mkdir 文件夹名			 于当前目录创建文件夹
		remov 文件名或文件夹名   删除文件或文件夹
		
软件目录结构
ftpserver
|	----__init__.py                 
|	----setup.py                       初始化数据文件
|	----bin                            
       |	----__init__.py
       |	----ftpserver.py           启动程序接口
|	----conf						   
	   |	----root.py				   用户数据文件管理
|	----core
       |	----__init__.py
	   |	----main.py                主程序
	   |	----lib.py                 工具模块
	   |	----cmd_shell.py           shell命令模块
|	----db
       |	----__init__.py
       |	----userdatabase           用户数据文件
       |	----calvin                 用户文件
       |	----tom                    用户文件
|	----README.txt                     说明文件


ftpclient
|	----__init__.py                 
|	----bin                            
       |	----__init__.py
       |	----ftpserver.py           启动接口
|	----core
       |	----__init__.py
	   |	----main.py                主程序
	   |	----lib.py                 工具模块
	   |	----shellorder.py          shell命令模块
|	----db							   用户下载目录
|	----README.txt                     说明文件

代码原理与结构
服务器端采用socketserver实现并发，客户端采用套接字与服务端实现数据通信，
采用tcp协议，
自制报头防止粘包现象
通过比较md5值保证文件一致性
1.			登录循环 login -------->主循环 handle / run
2.upload：
                 server                                      client
				 判断       <-----------------------报头（开始）
				
				1.空间不足
                  报头      >-----------------------end
				
				2.存在同名文件
						
						2.1同一文件 
						报头 >----------------------end

						2.2不完整文件
							报头  >-----------------比较md5
													
													同名不同质2.2.1							  
							end	  <-----------------报头
														
													短点续传  2.2.2
								  <-----------------报头
								  <-----------------文件
							报头  >-----------------end
				
				3.不存在同名文件
								  <-----------------文件
							报头  >-----------------end



