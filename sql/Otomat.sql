CREATE TABLE `report_list` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`HostName`  varchar(50) CHARACTER SET utf8 NULL DEFAULT NULL ,
`Host_ip`  varchar(16) CHARACTER SET utf8 NULL DEFAULT NULL ,
`Time`  timestamp NULL ON UPDATE CURRENT_TIMESTAMP ,
`Cpu_Utilization`  decimal(6,2) ZEROFILL NULL DEFAULT NULL ,
`Mem_total`  bigint(6) NULL DEFAULT NULL ,
`Mem_free`  bigint(6) NULL DEFAULT NULL ,
`Mem_used`  bigint(6) NULL DEFAULT NULL ,
`Mem_percent`  decimal(6,2) NULL DEFAULT NULL ,
`Swap_total`  bigint(6) NULL DEFAULT NULL ,
`Swap_free`  bigint(6) NULL DEFAULT NULL ,
`Swap_used`  bigint(6) NULL DEFAULT NULL ,
`Swap_percent`  decimal(6,2) NULL DEFAULT NULL ,
`Disk_total`  bigint(6) NULL DEFAULT NULL ,
`Disk_used`  bigint(6) NULL DEFAULT NULL ,
`Disk_free`  bigint(6) NULL DEFAULT NULL ,
`Disk_percent`  decimal(6,2) NULL DEFAULT NULL ,
`Network_traffic_recv`  bigint(6) NULL DEFAULT NULL ,
`Network_traffic_sent`  bigint(6) NULL DEFAULT NULL ,
PRIMARY KEY (`ID`)
)
;
