CREATE TABLE `report_list` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ServerName`  varchar(50) CHARACTER SET utf8 NULL DEFAULT NULL ,
`host_ip`  varchar(16) CHARACTER SET utf8 NULL DEFAULT NULL ,
`Time`  timestamp NULL ON UPDATE CURRENT_TIMESTAMP ,
`Cpu_Utilization`  decimal(6,2) ZEROFILL NULL DEFAULT NULL ,
`Mem_Total`  bigint(6) NULL DEFAULT NULL ,
`Mem_free`  bigint(6) NULL DEFAULT NULL ,
`Mem_Percent`  decimal(6,2) NULL DEFAULT NULL ,
`Swap_Total`  bigint(6) NULL DEFAULT NULL ,
`Swap_free`  bigint(6) NULL DEFAULT NULL ,
`Swap_Percent`  decimal(6,2) NULL DEFAULT NULL ,
`Disk_Total`  bigint(6) NULL DEFAULT NULL ,
`Disk_Used`  bigint(6) NULL DEFAULT NULL ,
`Disk_free`  bigint(6) NULL DEFAULT NULL ,
`Disk_Percent`  decimal(6,2) NULL DEFAULT NULL ,
`Network_traffic_recv`  bigint(6) NULL DEFAULT NULL ,
`Network_traffic_sent`  bigint(6) NULL DEFAULT NULL ,
PRIMARY KEY (`ID`)
)
;
