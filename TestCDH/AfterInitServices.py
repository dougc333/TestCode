#!/usr/bin/env python

#installs hdfs, hive, impala, yarn
#add scr; there is dfs_datanode_shortcircuit have to enable in cm 
#I dont see the enable SCR in the CM UI
#dont see fs.defautFS setting in CM UI
#test safety valve settings via python for fs.default.name and fs.defaultFS
#how to use final in python api


from cm_api.api_client import ApiResource
from cm_api.endpoints.clusters import ApiCluster
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.parcels import ApiParcel
from cm_api.endpoints.parcels import get_parcel
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from cm_api.endpoints.services import create_service
from cm_api.endpoints.types import ApiCommand, ApiRoleConfigGroupRef
from cm_api.endpoints.role_config_groups import get_role_config_group
from cm_api.endpoints.role_config_groups import ApiRoleConfigGroup
from cm_api.endpoints.roles import ApiRole
from time import sleep

#may have to replace w/hostid
CLUSTER_HOSTS=['r2341-d5-us02.dssd.com','r2341-d5-us03.dssd.com','r2341-d5-us04.dssd.com']
CM_HOST='r2341-d5-us01.dssd.com'

hosts = {
        'r2341-d5-us01.dssd.com': '86de389a-7182-4017-bab1-888ea2cff999',
        'r2341-d5-us02.dssd.com': '80366fcb-7a0a-448e-836e-d02e299e7975',
        'r2341-d5-us03.dssd.com': '79af8cf4-18e5-4192-b44b-fe7baa8e87a2',
        'r2341-d5-us04.dssd.com': '24b2bf04-e4f3-41b5-993c-0633f44b087c'
   }

#left out cm config, the cm config includes the parcel repo addresses which we update through the api
#this is not consistent with 'hdfs' in the role config groups hdfs-NAMENODE-BASE; 
HDFS_SERVICE_NAME = "HDFS"
HDFS_SERVICE_CONFIG = {
  'dfs_replication': 3,
  'dfs_permissions': 'false',
  #'io_compression_codecs': None,
  #'dfs_namenode_acls_enabled': None,
  #'hadoop_rpc_protection':None,
  #'hadoop_security_authorization':None,
  #'hadoop_sercurity_authentication':None,
  #'hadoop_ssl_require_client.cert':None,
  #'dfs_client_use_datanode_hostname':None,
  #'dfs_block_local_path_access_user': 'impala,hbase,mapred,spark'
}

DSSD_HDFS_SERVICE_CONFIG={
 u'com_dssd_hadoop_floodds_usablecapacity': '100000000000000',
 u'com_dssd_hadoop_floodds_volume': 'twu_vol',
 u'dfs_permissions': 'false',
 u'hdfs_service_config_safety_valve':  u'<property>\n<name>fs.defaultFS</name>\n<value>hdfs://r2341-d5-us01.dssd.com:8020</value>\n</property>',
 u'dfs_block_local_path_access_user': 'impala,hbase,mapred,spark'
}

hdfs_service_config={
u'service_config_suppression_core_site_safety_valve': None, 
u'service_config_suppression_navigator_client_config_safety_valve': None, 
u'dfs_ha_fencing_methods': None, 
u'navigator_client_max_num_audit_log': None, 
u'navigator_audit_log_max_file_size': None, 
u'service_config_suppression_yarn_proxy_user_groups_list': None, 
u'service_config_suppression_dfs_ha_proxy_provider': None, 
u'dfs_permissions': 'false', 
u'service_config_suppression_hdfs_service_env_safety_valve': None, 
u'process_username': None, 
u'hue_proxy_user_groups_list': None, 
u'hadoop_group_mapping_ldap_keystore_passwd': None, 
u'service_config_suppression_flume_proxy_user_groups_list': None, 
u'service_config_suppression_failovercontroller_count_validator': None, 
u'service_config_suppression_kerberos_princ_name': None, 
u'hue_proxy_user_hosts_list': None, 
u'service_config_suppression_oozie_proxy_user_groups_list': None, 
u'service_config_suppression_hadoop_authorized_admin_users': None, 
u'service_config_suppression_hdfs_replication_env_safety_valve': None, 
u'firehose_hdfs_canary_directory': None, 
u'audit_event_log_dir': None, 
u'hadoop_security_group_mapping': None, 
u'service_config_suppression_hadoop_http_auth_cookie_domain': None, 
u'yarn_proxy_user_groups_list': None, 
u'service_config_suppression_namenode_count_validator': None, 
u'oozie_proxy_user_groups_list': None, 
u'service_config_suppression_http_proxy_user_groups_list': None, 
u'hadoop_authorized_users': None, 
u'service_config_suppression_hadoop_ssl_validator': None, 
u'dfs_datanode_read_shortcircuit': None, 
u'service_config_suppression_navigator_event_tracker': None, 
u'hadoop_group_mapping_ldap_bind_user': None, 
u'enable_alerts': None, 
u'service_config_suppression_balancer_count_validator': None, 
u'ssl_client_truststore_password': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_bind_user': None, 
u'hadoop_group_mapping_ldap_bind_passwd': None, 
u'navigator_audit_queue_policy': None, 
u'service_config_suppression_nameservice_mountpoints_validator': None, 
u'catch_events': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_base': None, 
u'service_config_suppression_short_circuit_read_validator': None, 
u'redaction_policy_enabled': None, 
u'core_site_safety_valve': None, 
u'service_config_suppression_gateway_count_validator': None, 
u'service_config_suppression_hdfs_authentication_and_authorization_validator': None, 
u'service_config_suppression_smon_proxy_user_groups_list': None, 
u'service_config_suppression_dfs_block_local_path_access_user': None, 
u'service_config_suppression_process_groupname': None, 
u'hdfs_datanodes_healthy_thresholds': None, 
u'service_config_suppression_dfs_ha_fencing_ssh_private_key_files': None, 
u'service_config_suppression_datanode_count_validator': None, 
u'hue_kerberos_principal_shortname': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_group_filter': None, 
u'service_config_suppression_hue_kerberos_principal_shortname': None, 
u'smon_derived_configs_safety_valve': None, 
u'dfs_ha_proxy_provider': None, 
u'hadoop_http_auth_cookie_domain': None, 
u'service_config_suppression_ssl_server_keystore_location': None, 
u'hadoop_group_mapping_ldap_base': None, 
u'hdfs_proxy_user_hosts_list': None, 
u'service_config_suppression_nfsgateway_count_validator': None, 
u'service_health_suppression_hdfs_blocks_with_corrupt_replicas': None, 
u'navigator_audit_event_filter': None, 
u'hadoop_authorized_groups': None, 
u'dfs_encrypt_data_transfer_cipher_keybits': None, 
u'ssl_server_keystore_keypassword': None, 
u'hive_proxy_user_groups_list': None, 
u'oozie_proxy_user_hosts_list': None, 
u'service_health_suppression_hdfs_free_space_remaining': None, 
u'smon_proxy_user_hosts_list': None, 
u'hdfs_sentry_sync_path_prefixes': None, 
u'mapred_proxy_user_groups_list': None, 
u'hdfs_service_env_safety_valve': None, 
u'sentry_authorization_provider_hdfs_group': None, 
u'extra_auth_to_local_rules': None, 
u'ssl_server_keystore_password': None, 
u'dfs_webhdfs_enabled': None, 
u'service_config_suppression_hadoop_policy_config_safety_valve': None, 
u'service_config_suppression_hdfs_encryption_validator': None, 
u'service_config_suppression_hdfs_service_config_safety_valve': None, 
u'hadoop_secure_web_ui': None, 
u'hdfs_replication_haoop_env_sh_safety_valve': None, 
u'hdfs_proxy_user_groups_list': None, 
u'hadoop_rpc_protection': None, 
u'service_config_suppression_hue_proxy_user_hosts_list': None, 
u'ssl_client_truststore_location': None, 
u'hadoop_authorized_admin_users': None, 
u'hdfs_missing_blocks_thresholds': None, 
u'hdfs_namenode_activation_startup_tolerance': None, 
u'redaction_policy': None, 
u'yarn_proxy_user_hosts_list': None, 
u'httpfs_proxy_user_groups_list': None, 
u'flume_proxy_user_groups_list': None, 
u'mapred_proxy_user_hosts_list': None, 
u'smon_client_config_overrides': None, 
u'service_triggers': None, 
u'service_config_suppression_hdfs_proxy_user_groups_list': None, 
u'service_config_suppression_process_username': None, 
u'hdfs_hadoop_ssl_enabled': None, 
u'trusted_realms': None, 
u'service_health_suppression_hdfs_failover_controllers_healthy': None, 
u'service_config_suppression_smon_proxy_user_hosts_list': None, 
u'dfs_client_use_datanode_hostname': None, 
u'failover_controllers_healthy_enabled': None, 
u'hadoop_group_mapping_ldap_member_attr': None, 
u'dfs_block_local_path_access_user': None, 
u'dfs_ha_fencing_cloudera_manager_timeout_millis': None, 
u'navigator_audit_enabled': None, 
u'dfs_image_transfer_bandwidthPerSec': None, 
u'service_config_suppression_mapred_proxy_user_groups_list': None, 
u'hdfs_user_to_impersonate': None, 
u'hadoop_group_mapping_ldap_keystore': None, 
u'service_config_suppression_hdfs_sentry_sync_path_prefixes': None, 
u'service_config_suppression_navigator_audit_event_filter': None, 
u'service_config_suppression_ssl_client_truststore_password': None, 
u'dfs_permissions_supergroup': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_url': None, 
u'smon_proxy_user_groups_list': None, 
u'service_config_suppression_hadoop_authorized_groups': None, 
u'service_config_suppression_httpfs_proxy_user_hosts_list': None, 
u'dfs_replication_min': '3', 
u'hdfs_free_space_thresholds': None, 
u'service_config_suppression_hdfs_hadoop_group_name': None, 
u'service_config_suppression_ssl_server_keystore_password': None, 
u'service_config_suppression_single_user_mode_override_validator': None, 
u'dfs_replication_max': '3', 
u'service_config_suppression_smon_client_config_overrides': None, 
u'HTTP_proxy_user_hosts_list': None, 
u'firehose_hdfs_canary_directory_permissions': None, 
u'hadoop_security_authorization': None, 
u'kms_service': None, 
u'hadoop_group_mapping_ldap_group_name_attr': None, 
u'dfs_datanode_hdfs_blocks_metadata_enabled': None, 
u'service_config_suppression_httpfs_proxy_user_groups_list': None, 
u'hdfs_active_namenode_detecton_window': None, 
u'service_config_suppression_flume_proxy_user_hosts_list': None, 
u'dfs_replication': '3', 
u'HTTP_proxy_user_groups_list': None, 
u'hdfs_hadoop_group_name': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_user_filter': None, 
u'service_config_suppression_dfs_ha_fencing_methods': None, 
u'service_config_suppression_hive_proxy_user_hosts_list': None, 
u'service_config_suppression_dfs_permissions_supergroup': None, 
u'dfs_namenode_acls_enabled': None, 
u'service_config_suppression_service_triggers': None, 
u'service_config_suppression_io_compression_codecs': None, 
u'hadoop_group_mapping_ldap_user_filter': None, 
u'ssl_server_keystore_location': None, 
u'service_config_suppression_journalnode_count_validator': None, 
u'service_config_suppression_hdfs_proxy_user_hosts_list': None, 
u'service_config_suppression_firehose_hdfs_canary_directory_permissions': None,
u'navigator_event_tracker': None, 
u'service_config_suppression_firehose_hdfs_canary_directory': None, 
u'hdfs_replication_env_safety_valve': None, 
u'dfs_block_size': None, 
u'service_config_suppression_hue_proxy_user_groups_list': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_keystore_passwd': None, 
u'dfs_domain_socket_path': None, 
u'service_config_suppression_hdfs_user_home_dir': None, 
u'dfs_encrypt_data_transfer_algorithm': None, 
u'hdfs_under_replicated_blocks_thresholds': None, 
u'service_health_suppression_hdfs_data_nodes_healthy': None, 
u'hdfs_service_config_safety_valve':  u'<property>\n<name>fs.defaultFS</name>\n<value>hdfs://r2341-d5-us01.dssd.com:8020</value>\n</property>',
u'service_config_suppression_yarn_proxy_user_hosts_list': None, 
u'service_health_suppression_hdfs_canary_health': None, 
u'dfs_encrypt_data_transfer': None, 
u'service_config_suppression_hdfs_ssl_client_safety_valve': None, 
u'service_config_suppression_httpfs_count_validator': None, 
u'service_config_suppression_secondarynamenode_count_validator': None, 
u'dfs_client_file_block_storage_locations_timeout': None, 
u'service_config_suppression_sentry_authorization_provider_hdfs_group': None, 
u'io_compression_codecs': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_member_attr': None, 
u'service_config_suppression_nameservice_namenodes_heap_size_validator': None, 
u'hadoop_security_authentication': None, 
u'service_config_suppression_dfs_replication': None, 
u'hadoop_policy_config_safety_valve': None, 
u'service_config_suppression_redaction_policy': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_bind_passwd': None, 
u'hdfs_namenode_health_enabled': None, 
u'hdfs_ssl_server_safety_valve': None, 
u'hdfs_user_home_dir': None, 
u'service_health_suppression_hdfs_missing_blocks': None, 
u'dfs_data_transfer_protection': None, 
u'service_config_suppression_hadoop_authorized_users': None, 
u'flume_proxy_user_hosts_list': None, 
u'hadoop_group_mapping_ldap_url': None, 
u'dfs_ha_fencing_ssh_connect_timeout': None, 
u'hdfs_sentry_sync_enable': None, 
u'httpfs_proxy_user_hosts_list': None, 
u'enable_config_alerts': None, 
u'zookeeper_service': None, 
u'service_config_suppression_smon_derived_configs_safety_valve': None, 
u'service_config_suppression_hadoop_authorized_admin_groups': None, 
u'service_config_suppression_mapred_proxy_user_hosts_list': None, 
u'dfs_image_transfer_timeout': None, 
u'service_config_suppression_auto_failover_validator': None, 
u'kerberos_princ_name': None, 
u'service_config_suppression_nameservice_checkpoint_configuration_validator': None, 
u'service_config_suppression_oozie_proxy_user_hosts_list': None, 
u'service_config_suppression_http_proxy_user_hosts_list': None, 
u'process_groupname': None, 
u'hive_proxy_user_hosts_list': None, 
u'service_config_suppression_trusted_realms': None, 
u'service_config_suppression_nfs_ha_validator': None, 
u'log_event_retry_frequency': None, 
u'service_health_suppression_hdfs_ha_namenode_health': None, 
u'dfs_umaskmode': None, 
u'service_config_suppression_dfs_domain_socket_path': None, 
u'service_config_suppression_hdfs_user_to_impersonate': None, 
u'service_config_suppression_hive_proxy_user_groups_list': None, 
u'service_config_suppression_audit_event_log_dir': None, 
u'hdfs_canary_health_enabled': None, 
u'hdfs_blocks_with_corrupt_replicas_thresholds': None, 
u'hadoop_authorized_admin_groups': None, 
u'hadoop_group_mapping_ldap_group_filter': None, 
u'service_config_suppression_extra_auth_to_local_rules': None, 
u'service_config_suppression_ssl_client_truststore_location': None, 
u'service_config_suppression_hdfs_ssl_server_safety_valve': None, 
u'service_health_suppression_hdfs_under_replicated_blocks': None, 
u'navigator_client_config_safety_valve': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_group_name_attr': None, 
u'hdfs_standby_namenodes_health_enabled': None, 
u'dfs_ha_fencing_ssh_private_key_files': None, 
u'service_config_suppression_hdfs_replication_haoop_env_sh_safety_valve': None, 
u'hadoop_group_mapping_ldap_use_ssl': None, 
u'service_config_suppression_ssl_server_keystore_keypassword': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_keystore': None, 
u'hdfs_ssl_client_safety_valve': None, 
u'service_config_suppression_redaction_policy_validator': None
}

dssd_hdfs_service_config={
u'com_dssd_hadoop_floodds_usablecapacity': None, 
u'service_config_suppression_core_site_safety_valve': None, 
u'service_config_suppression_navigator_client_config_safety_valve': None, 
u'dfs_ha_fencing_methods': None, 
u'navigator_client_max_num_audit_log': None, 
u'navigator_audit_log_max_file_size': None, 
u'service_config_suppression_yarn_proxy_user_groups_list': None, 
u'service_config_suppression_dfs_ha_proxy_provider': None, 
u'dfs_permissions': None, 
u'service_config_suppression_hdfs_service_env_safety_valve': None, 
u'process_username': None, 
u'hue_proxy_user_groups_list': None,
u'hadoop_group_mapping_ldap_keystore_passwd': None, 
u'service_config_suppression_flume_proxy_user_groups_list': None, 
u'service_config_suppression_failovercontroller_count_validator': None, 
u'service_config_suppression_kerberos_princ_name': None, 
u'hue_proxy_user_hosts_list': None, 
u'service_config_suppression_oozie_proxy_user_groups_list': None, 
u'service_config_suppression_hadoop_authorized_admin_users': None, 
u'service_config_suppression_hdfs_replication_env_safety_valve': None, 
u'firehose_hdfs_canary_directory': None, 
u'audit_event_log_dir': None, 
u'hadoop_security_group_mapping': None, 
u'service_config_suppression_hadoop_http_auth_cookie_domain': None, 
u'yarn_proxy_user_groups_list': None, 
u'service_config_suppression_namenode_count_validator': None, 
u'oozie_proxy_user_groups_list': None, 
u'service_config_suppression_http_proxy_user_groups_list': None, 
u'hadoop_authorized_users': None, 
u'service_config_suppression_hadoop_ssl_validator': None, 
u'service_config_suppression_navigator_event_tracker': None, 
u'hadoop_group_mapping_ldap_bind_user': None, 
u'enable_alerts': None, 
u'service_config_suppression_balancer_count_validator': None, 
u'ssl_client_truststore_password': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_bind_user': None, 
u'hadoop_group_mapping_ldap_bind_passwd': None, 
u'navigator_audit_queue_policy': None, 
u'service_config_suppression_nameservice_mountpoints_validator': None, 
u'catch_events': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_base': None, 
u'service_config_suppression_short_circuit_read_validator': None, 
u'redaction_policy_enabled': None, 
u'core_site_safety_valve': None, 
u'service_config_suppression_gateway_count_validator': None, 
u'service_config_suppression_hdfs_authentication_and_authorization_validator': None, 
u'service_config_suppression_smon_proxy_user_groups_list': None, 
u'service_config_suppression_dfs_block_local_path_access_user': None, 
u'service_config_suppression_process_groupname': None, 
u'hdfs_datanodes_healthy_thresholds': None, 
u'service_config_suppression_dfs_ha_fencing_ssh_private_key_files': None, 
u'dfs_webhdfs_enabled': None, 
u'hue_kerberos_principal_shortname': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_group_filter': None, 
u'service_config_suppression_hue_kerberos_principal_shortname': None, 
u'smon_derived_configs_safety_valve': None, 
u'dfs_ha_proxy_provider': None, 
u'hadoop_http_auth_cookie_domain': None, 
u'service_config_suppression_ssl_server_keystore_location': None, 
u'hadoop_group_mapping_ldap_base': None, 
u'hdfs_proxy_user_hosts_list': None, 
u'service_config_suppression_nfsgateway_count_validator': None, 
u'service_health_suppression_hdfs_blocks_with_corrupt_replicas': None, 
u'navigator_audit_event_filter': None, 
u'hadoop_authorized_groups': None, 
u'dfs_encrypt_data_transfer_cipher_keybits': None, 
u'ssl_server_keystore_keypassword': None, 
u'hive_proxy_user_groups_list': None, 
u'oozie_proxy_user_hosts_list': None, 
u'service_health_suppression_hdfs_free_space_remaining': None, 
u'smon_proxy_user_hosts_list': None, 
u'hdfs_sentry_sync_path_prefixes': None, 
u'mapred_proxy_user_groups_list': None, 
u'hdfs_service_env_safety_valve': None, 
u'sentry_authorization_provider_hdfs_group': None, 
u'extra_auth_to_local_rules': None, 
u'ssl_server_keystore_password': None, 
u'service_config_suppression_hadoop_policy_config_safety_valve': None, 
u'service_config_suppression_hdfs_encryption_validator': None, 
u'service_config_suppression_hdfs_service_config_safety_valve': None, 
u'hadoop_secure_web_ui': None, 
u'hdfs_replication_haoop_env_sh_safety_valve': None, 
u'hdfs_proxy_user_groups_list': None, 
u'hadoop_rpc_protection': None, 
u'service_config_suppression_hue_proxy_user_hosts_list': None, 
u'ssl_client_truststore_location': None, 
u'hadoop_authorized_admin_users': None, 
u'hdfs_missing_blocks_thresholds': None, 
u'hdfs_namenode_activation_startup_tolerance': None, 
u'com_dssd_hadoop_floodds_volume': u'twu_vol', 
u'redaction_policy': None, 
u'yarn_proxy_user_hosts_list': None, 
u'httpfs_proxy_user_groups_list': None, 
u'flume_proxy_user_groups_list': None, 
u'mapred_proxy_user_hosts_list': None, 
u'smon_client_config_overrides': None, 
u'service_triggers': None, 
u'service_config_suppression_hdfs_proxy_user_groups_list': None, 
u'service_config_suppression_process_username': None, 
u'hdfs_hadoop_ssl_enabled': None, 
u'trusted_realms': None, 
u'service_health_suppression_hdfs_failover_controllers_healthy': None, 
u'service_config_suppression_smon_proxy_user_hosts_list': None,
u'dfs_client_use_datanode_hostname': None, 
u'failover_controllers_healthy_enabled': None, 
u'hadoop_group_mapping_ldap_member_attr': None, 
u'dfs_block_local_path_access_user': None, 
u'dfs_ha_fencing_cloudera_manager_timeout_millis': None, 
u'navigator_audit_enabled': None, 
u'dfs_image_transfer_bandwidthPerSec': None, 
u'service_config_suppression_mapred_proxy_user_groups_list': None, 
u'hdfs_user_to_impersonate': None, 
u'hadoop_group_mapping_ldap_keystore': None, 
u'service_config_suppression_hdfs_sentry_sync_path_prefixes': None, 
u'service_config_suppression_navigator_audit_event_filter': None, 
u'service_config_suppression_ssl_client_truststore_password': None, 
u'dfs_permissions_supergroup': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_url': None, 
u'smon_proxy_user_groups_list': None, 
u'service_config_suppression_hadoop_authorized_groups': None, 
u'service_config_suppression_httpfs_proxy_user_hosts_list': None, 
u'dfs_replication_min': None, 
u'service_config_suppression_hdfs_hadoop_group_name': None, 
u'service_config_suppression_ssl_server_keystore_password': None, 
u'service_config_suppression_single_user_mode_override_validator': None, 
u'dfs_replication_max': None, 
u'service_config_suppression_smon_client_config_overrides': None, 
u'HTTP_proxy_user_hosts_list': None, 
u'firehose_hdfs_canary_directory_permissions': None, 
u'hadoop_security_authorization': None, 
u'kms_service': None, 
u'hadoop_group_mapping_ldap_group_name_attr': None, 
u'service_config_suppression_httpfs_proxy_user_groups_list': None, 
u'hdfs_active_namenode_detecton_window': None, 
u'service_config_suppression_flume_proxy_user_hosts_list': None, 
u'dfs_replication': None, 
u'HTTP_proxy_user_groups_list': None, 
u'hdfs_hadoop_group_name': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_user_filter': None, 
u'service_config_suppression_dfs_ha_fencing_methods': None, 
u'service_config_suppression_hive_proxy_user_hosts_list': None, 
u'service_config_suppression_dfs_permissions_supergroup': None, 
u'dfs_namenode_acls_enabled': None, 
u'service_config_suppression_service_triggers': None, 
u'service_config_suppression_io_compression_codecs': None, 
u'hadoop_group_mapping_ldap_user_filter': None, 
u'ssl_server_keystore_location': None, 
u'service_config_suppression_journalnode_count_validator': None, 
u'service_config_suppression_hdfs_proxy_user_hosts_list': None, 
u'service_config_suppression_firehose_hdfs_canary_directory_permissions': None, 
u'navigator_event_tracker': None, 
u'service_config_suppression_firehose_hdfs_canary_directory': None, 
u'hdfs_replication_env_safety_valve': None, 
u'dfs_block_size': None, 
u'service_config_suppression_hue_proxy_user_groups_list': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_keystore_passwd': None, 
u'service_config_suppression_hdfs_user_home_dir': None, 
u'dfs_encrypt_data_transfer_algorithm': None, 
u'hdfs_under_replicated_blocks_thresholds': None, 
u'service_health_suppression_hdfs_data_nodes_healthy': None, 
u'hdfs_service_config_safety_valve': None, 
u'service_config_suppression_yarn_proxy_user_hosts_list': None, 
u'service_health_suppression_hdfs_canary_health': None, 
u'dfs_encrypt_data_transfer': None, 
u'service_config_suppression_hdfs_ssl_client_safety_valve': None, 
u'service_config_suppression_httpfs_count_validator': None, 
u'service_config_suppression_secondarynamenode_count_validator': None, 
u'dfs_client_file_block_storage_locations_timeout': None, 
u'service_config_suppression_sentry_authorization_provider_hdfs_group': None, 
u'io_compression_codecs': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_member_attr': None, 
u'service_config_suppression_nameservice_namenodes_heap_size_validator': None, 
u'hadoop_security_authentication': None, 
u'service_config_suppression_dfs_replication': None, 
u'hadoop_policy_config_safety_valve': None, 
u'service_config_suppression_redaction_policy': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_bind_passwd': None, 
u'hdfs_namenode_health_enabled': None, 
u'hdfs_ssl_server_safety_valve': None, 
u'hdfs_user_home_dir': None, 
u'service_health_suppression_hdfs_missing_blocks': None, 
u'dfs_data_transfer_protection': None, 
u'service_config_suppression_hadoop_authorized_users': None, 
u'flume_proxy_user_hosts_list': None, 
u'hadoop_group_mapping_ldap_url': None, 
u'dfs_ha_fencing_ssh_connect_timeout': None, 
u'hdfs_sentry_sync_enable': None, 
u'httpfs_proxy_user_hosts_list': None, 
u'enable_config_alerts': None, 
u'zookeeper_service': None, 
u'service_config_suppression_smon_derived_configs_safety_valve': None, 
u'service_config_suppression_com_dssd_hadoop_floodds_volume': None, 
u'service_config_suppression_hadoop_authorized_admin_groups': None, 
u'service_config_suppression_mapred_proxy_user_hosts_list': None, 
u'dfs_image_transfer_timeout': None, 
u'service_config_suppression_auto_failover_validator': None, 
u'kerberos_princ_name': None, 
u'service_config_suppression_nameservice_checkpoint_configuration_validator': None, 
u'service_config_suppression_oozie_proxy_user_hosts_list': None, 
u'service_config_suppression_http_proxy_user_hosts_list': None, 
u'process_groupname': None, 
u'hive_proxy_user_hosts_list': None, 
u'service_config_suppression_trusted_realms': None, 
u'service_config_suppression_nfs_ha_validator': None, 
u'service_config_suppression_dssddatanode_count_validator': None, 
u'log_event_retry_frequency': None, 
u'service_health_suppression_hdfs_ha_namenode_health': None, 
u'dfs_umaskmode': None, 
u'hdfs_free_space_thresholds': None, 
u'service_config_suppression_hdfs_user_to_impersonate': None, 
u'service_config_suppression_hive_proxy_user_groups_list': None, 
u'service_config_suppression_audit_event_log_dir': None, 
u'hdfs_canary_health_enabled': None, 
u'hdfs_blocks_with_corrupt_replicas_thresholds': None, 
u'hadoop_authorized_admin_groups': None, 
u'hadoop_group_mapping_ldap_group_filter': None, 
u'service_config_suppression_extra_auth_to_local_rules': None, 
u'service_config_suppression_ssl_client_truststore_location': None, 
u'service_config_suppression_hdfs_ssl_server_safety_valve': None, 
u'service_health_suppression_hdfs_under_replicated_blocks': None, 
u'navigator_client_config_safety_valve': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_group_name_attr': None, 
u'hdfs_standby_namenodes_health_enabled': None, 
u'dfs_ha_fencing_ssh_private_key_files': None, 
u'service_config_suppression_hdfs_replication_haoop_env_sh_safety_valve': None, 
u'hadoop_group_mapping_ldap_use_ssl': None, 
u'service_config_suppression_ssl_server_keystore_keypassword': None, 
u'service_config_suppression_hadoop_group_mapping_ldap_keystore': None, 
u'hdfs_ssl_client_safety_valve': None, 
u'service_config_suppression_redaction_policy_validator': None}




HDFS_NAMENODE_SERVICE_NAME = "nn"
HDFS_NAMENODE_HOST = CM_HOST
HDFS_NAMENODE_CONFIG = {
  u'dfs_name_dir_list': '/testdir/dfs/nn',
  u'dfs_namenode_handler_count': u'30',
  u'dfs_namenode_servicerpc_address': u'8022',
}

hdfs_NAMENODE_BASE_CONFIG={
u'role_health_suppression_name_node_ha_checkpoint_age': None, 
u'dfs_namenode_quorum_journal_name': None, 
u'stacks_collection_enabled': None, 
u'dfs_namenode_avoid_read_stale_datanode': None, 
u'dfs_http_port': None, 
u'role_config_suppression_namenode_java_opts': None, 
u'stacks_collection_method': None, 
u'role_health_suppression_name_node_heap_dump_directory_free_space': None, 
u'namenode_web_metric_collection_thresholds': None, 
u'namenode_rpc_latency_thresholds': None, 
u'namenode_pause_duration_window': None, 
u'role_health_suppression_name_node_log_directory_free_space': None, 
u'unexpected_exits_window': None, 
u'role_health_suppression_name_node_rpc_latency': None, 
u'role_health_suppression_name_node_file_descriptor': None, 
u'dfs_namenode_replication_max_streams': None, 
u'log4j_safety_valve': None, 
u'dfs_namenode_write_stale_datanode_ratio': None, 
u'namenode_checkpoint_transactions_thresholds': None, 
u'namenode_pause_duration_thresholds': None, 
u'role_health_suppression_name_node_swap_memory_usage': None, 
u'enable_alerts': None, 
u'role_health_suppression_name_node_data_directories_free_space': None, 
u'role_config_suppression_fs_trash_interval_minimum_validator': None, 
u'role_config_suppression_namenode_config_safety_valve': None, 
u'role_health_suppression_name_node_safe_mode': None, 
u'role_health_suppression_name_node_web_metric_collection': None, 
u'role_config_suppression_dfs_namenode_plugins_list': None, 
u'role_config_suppression_dfs_federation_namenode_nameservice': None, 
u'namenode_rolling_upgrade_status_enabled': None, 
u'nameservice_mountpoints': None, 
u'namenode_fd_thresholds': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'log_directory_free_space_percentage_thresholds': None, 
u'log_event_whitelist': None, 
u'namenode_safe_mode_enabled': None, 
u'role_config_suppression_dfs_namenode_edits_dir': None, 
u'role_config_suppression_namenode_hosts_exclude_safety_valve': None, 
u'role_config_suppression_dfs_namenode_service_handler_count_minimum_validator': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'namenode_java_heapsize': None, 
u'role_config_suppression_role_triggers': None, 
u'role_health_suppression_name_node_journal_node_sync_status': None, 
u'max_log_size': None, 
u'dfs_name_dir_list': 
u'/testdir/dfs/nn', 
u'role_health_suppression_name_node_upgrade_status': None, 
u'role_config_suppression_dfs_namenode_shared_edits_dir': None, 
u'dfs_namenode_stale_datanode_interval': None, 
u'role_health_suppression_name_node_pause_duration': None, 
u'namenode_port': None, 
u'hadoop_metrics2_safety_valve': None, 
u'stacks_collection_data_retention': None, 
u'stacks_collection_frequency': None, 
u'namenode_rpc_latency_window': None, 
u'dfs_namenode_servicerpc_address': u'8022', 
u'role_config_suppression_dfs_namenode_quorum_journal_name': None, 
u'namenode_out_of_sync_journal_nodes_thresholds': None, 
u'unexpected_exits_thresholds': None, 
u'namenode_checkpoint_age_thresholds': None, 
u'role_config_suppression_hadoop_metrics2_safety_valve': None, 
u'namenode_scm_health_enabled': None, 
u'dfs_namenode_replication_max_streams_hard_limit': None, 
u'NAMENODE_role_env_safety_valve': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'namenode_log_dir': None, 
u'rm_cpu_shares': None, 
u'namenode_upgrade_status_enabled': None, 
u'dfs_federation_namenode_nameservice': None, 
u'log_threshold': None, 
u'dfs_safemode_threshold_pct': None, 
u'dfs_namenode_edits_dir': None, 
u'dfs_name_dir_restore': None, 
u'namenode_startup_tolerance': None, 
u'namenode_java_opts': None, 
u'role_config_suppression_namenode_java_heapsize_minimum_validator': None, 
u'autofailover_enabled': None, 
u'namenode_data_directories_free_space_percentage_thresholds': None, 
u'namenode_hosts_exclude_safety_valve': None, 
u'namenode_data_directories_free_space_absolute_thresholds': None, 
u'role_config_suppression_namenode_role_env_safety_valve': None, 
u'role_health_suppression_name_node_rolling_upgrade_status': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'dfs_namenode_invalidate_work_pct_per_iteration': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'rm_memory_hard_limit': None, 
u'namenode_web_metric_collection_enabled': None, 
u'dfs_qjournal_write_txns_timeout_ms': None, 
u'process_swap_memory_thresholds': None, 
u'fs_checkpoint_period': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'rlimit_fds': None, 
u'dfs_access_time_precision': None, 
u'dfs_thrift_threads_min': None, 
u'role_config_suppression_topology_script_file_name': None, 
u'dfs_thrift_threads_max': None, 
u'role_config_suppression_dfs_namenode_handler_count_minimum_validator': None, 
u'topology_script_file_name': None, 
u'oom_heap_dump_dir': None, 
u'namenode_blockstatechange_log_threshold': None, 
u'dfs_namenode_avoid_write_stale_datanode': None, 
u'namenode_directory_failures_thresholds': None, 
u'role_health_suppression_name_node_unexpected_exits': None, 
u'fs_trash_interval': None, 
u'namenode_config_safety_valve': None, 
u'dfs_namenode_replication_work_multiplier_per_iteration': None, 
u'max_log_backup_index': None, 
u'dfs_safemode_extension': None, 
u'dfs_thrift_timeout': None, 
u'rm_memory_soft_limit': None, 
u'oom_heap_dump_enabled': None, 
u'dfs_namenode_service_handler_count': None, 
u'role_config_suppression_namenode_hosts_allow_safety_valve': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'role_config_suppression_dfs_name_dir_list': None, 
u'fs_checkpoint_txns': None, 
u'namenode_host_health_enabled': None, 
u'oom_sigkill_enabled': None, 
u'role_health_suppression_name_node_scm_health': None, 
u'dfs_https_port': None, 
u'namenode_hosts_allow_safety_valve': None, 
u'role_config_suppression_nameservice_mountpoints': None, 
u'role_triggers': None, 
u'enable_config_alerts': None, 
u'namenode_bind_wildcard': None, 
u'dfs_namenode_plugins_list': None, 
u'role_health_suppression_name_node_host_health': None, 
u'dfs_namenode_shared_edits_dir': None, 
u'stacks_collection_directory': None, 
u'rm_io_weight': None, 
u'dfs_namenode_handler_count': None, 
u'role_config_suppression_namenode_log_dir': None, 
u'role_health_suppression_name_node_directory_failures': None, 
u'dfs_safemode_min_datanodes': None
}



HDFS_SECONDARY_NAMENODE_HOST = CM_HOST
HDFS_SECONDARY_NAMENODE_CONFIG = {
  'fs_checkpoint_dir_list': '/testdir/dfs/snn'
}

hdfs_SECONDARY_NAMENODE_BASE_CONFIG={
u'log_directory_free_space_percentage_thresholds': None, 
u'log_event_whitelist': None, 
u'role_health_suppression_secondary_name_node_web_metric_collection': None, 
u'secondarynamenode_java_opts': None, 
u'stacks_collection_enabled': None, 
u'secondarynamenode_checkpoint_directories_free_space_absolute_thresholds': None, 
u'secondary_namenode_java_heapsize': None, 
u'role_config_suppression_dfs_secondarynamenode_nameservice': None, 
u'role_health_suppression_secondary_name_node_scm_health': None, 
u'secondarynamenode_gc_duration_thresholds': None, 
u'role_config_suppression_secondarynamenode_config_safety_valve': None, 
u'role_health_suppression_secondary_name_node_heap_dump_directory_free_space': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'stacks_collection_method': None, 
u'role_config_suppression_secondarynamenode_log_dir': None, 
u'secondarynamenode_scm_health_enabled': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'fs_checkpoint_txns': None, 
u'role_config_suppression_fs_checkpoint_dir_list': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'rm_memory_soft_limit': None, 
u'secondarynamenode_web_metric_collection_enabled': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'secondarynamenode_config_safety_valve': None, 
u'role_config_suppression_secondarynamenode_java_opts': None, 
u'role_health_suppression_secondary_name_node_swap_memory_usage': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'rm_memory_hard_limit': None, 
u'process_swap_memory_thresholds': None, 
u'unexpected_exits_window': None, 
u'rm_io_weight': None, 
u'role_health_suppression_secondary_name_node_gc_duration': None, 
u'hadoop_metrics2_safety_valve': None, 
u'stacks_collection_data_retention': None, 
u'SECONDARYNAMENODE_role_env_safety_valve': None, 
u'role_health_suppression_secondary_name_node_unexpected_exits': None, 
u'secondary_namenode_bind_wildcard': None, 
u'log4j_safety_valve': None, 
u'role_config_suppression_role_triggers': None, 
u'fs_checkpoint_period': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'role_config_suppression_secondarynamenode_role_env_safety_valve': None, 
u'role_health_suppression_secondary_name_node_checkpoint_directories_free_space': None, 
u'rlimit_fds': None, 
u'role_health_suppression_secondary_name_node_host_health': None, 
u'secondarynamenode_web_metric_collection_thresholds': None, 
u'enable_alerts': None, 
u'secondarynamenode_checkpoint_directories_free_space_percentage_thresholds': None, 
u'secondarynamenode_host_health_enabled': None, 
u'max_log_size': None, 
u'oom_sigkill_enabled': None, 
u'oom_heap_dump_enabled': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'unexpected_exits_thresholds': None, 
u'role_health_suppression_secondary_name_node_file_descriptor': None, 
u'secondarynamenode_fd_thresholds': None, 
u'role_config_suppression_hadoop_metrics2_safety_valve': None, 
u'secondarynamenode_gc_duration_window': None, 
u'role_triggers': None, 
u'enable_config_alerts': None, 
u'role_health_suppression_secondary_name_node_log_directory_free_space': None, 
u'fs_checkpoint_dir_list': u'/testdir/dfs/snn', 
u'stacks_collection_directory': None, 
u'max_log_backup_index': None, 
u'rm_cpu_shares': None, 
u'oom_heap_dump_dir': None, 
u'stacks_collection_frequency': None, 
u'dfs_secondarynamenode_nameservice': None, 
u'log_threshold': None, 
u'dfs_secondary_https_port': None, 
u'secondarynamenode_log_dir': None, 
u'dfs_secondary_http_port': None
 }



# this isnt right, should be 3; what is format for hosts? 
HDFS_DATANODE_HOSTS = list(CLUSTER_HOSTS)
#dfs_datanode_du_reserved must be smaller than the amount of free space across the data dirs
#Ideally each data directory will have at least 1TB capacity; they need at least 100GB at a minimum 
#dfs_datanode_failed_volumes_tolerated must be less than the number of different data dirs (ie volumes) in dfs_data_dir_list

HDFS_DATANODE_CONFIG = {
  'dfs_data_dir_list': '/testdir/dfs/dn',
  'dfs_datanode_handler_count': 30,
  'dfs_datanode_du_reserved': 1073741824,
  'dfs_datanode_failed_volumes_tolerated': 0,
  'dfs_datanode_data_dir_perm': 755,
}

DSSD_DATANODE_CONFIG={
  #u'dfs_datanode_max_xcievers': None,
  #u'datanode_java_heapsize': None,
  #u'datanode_log_dir': None,
  #u'dfs_datanode_readahead_bytes': None,
  #u'dfs_datanode_https_port': None,
  u'com_dssd_flood_conn_cpus': '26,28,30',
  #u'datanode_java_opts': None,
  #u'max_log_size': '200MB',
  #u'dfs_datanode_handler_count': None,
  u'com_dssd_flood_conn_client_qdepth': 64,
}


#this may be different than hdfs_DATANODE_BASE_CONFIG
hdfs_DATANODE_BASE_CONFIG={
u'dfs_datanode_max_xcievers': None, 
u'stacks_collection_enabled': None, 
u'dfs_datanode_drop_cache_behind_reads': None, 
u'stacks_collection_method': None, 
u'role_health_suppression_dssd_data_node_ha_connectivity': None, 
u'dfs_datanode_use_datanode_hostname': None, 
u'dssddatanode_web_metric_collection_enabled': None, 
u'log4j_safety_valve': None, 
u'dssddatanode_host_health_enabled': None, 
u'unexpected_exits_window': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'datanode_java_heapsize': None, 
u'role_health_suppression_dssd_data_node_scm_health': None, 
u'datanode_log_dir': None, 
u'enable_config_alerts': None, 
u'dfs_datanode_readahead_bytes': None, 
u'dfs_datanode_https_port': None, 
u'oom_heap_dump_enabled': None, 
u'dfs_balance_bandwidthPerSec': None, 
u'datanode_transceivers_usage_thresholds': None, 
u'role_config_suppression_com_dssd_flood_conn_cpus': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'com_dssd_flood_conn_cpus': None, 
u'log_event_whitelist': None, 
u'dssddatanode_web_metric_collection_thresholds': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'dssddatanode_pause_duration_window': None, 
u'role_config_suppression_datanode_java_opts': None, 
u'max_log_size': '200MB', 
u'role_triggers': None, 
u'datanode_java_opts': None, 
u'role_config_suppression_dfs_datanode_plugins_list': None, 
u'hadoop_metrics2_safety_valve': None, 
u'stacks_collection_data_retention': None, 
u'dfs_datanode_http_port': None, 
u'unexpected_exits_thresholds': None, 
u'com_dssd_flood_conn_qmax': None, 
u'role_config_suppression_hadoop_metrics2_safety_valve': None, 
u'dfs_datanode_port': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'rm_cpu_shares': None, 
u'log_threshold': None, 
u'dssddatanode_fd_thresholds': None, 
u'role_health_suppression_dssd_data_node_file_descriptor': None, 
u'role_config_suppression_datanode_failed_volumes_validator': None, 
u'role_health_suppression_dssd_data_node_heap_dump_directory_free_space': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'rm_memory_hard_limit': None, 
u'dfs_datanode_plugins_list': None, 
u'process_swap_memory_thresholds': None, 
u'rlimit_fds': None, 
u'role_config_suppression_datanode_reserved_space_validator': None, 
u'datanode_config_safety_valve': None, 
u'datanode_connectivity_health_enabled': None, 
u'dfs_thrift_threads_min': None, 
u'role_config_suppression_datanode_config_safety_valve': None, 
u'role_config_suppression_dssddatanode_role_env_safety_valve': None, 
u'datanode_connectivity_tolerance': None, 
u'role_health_suppression_dssd_data_node_host_health': None, 
u'dfs_thrift_threads_max': '4096', 
u'role_health_suppression_dssd_data_node_unexpected_exits': None, 
u'oom_heap_dump_dir': None, 
u'stacks_collection_frequency': None, 
u'role_health_suppression_dssd_data_node_swap_memory_usage': None, 
u'dfs_datanode_sync_behind_writes': None, 
u'role_health_suppression_dssd_data_node_web_metric_collection': None, 
u'role_health_suppression_dssd_data_node_transceivers_usage': None, 
u'dfs_datanode_drop_cache_behind_writes': None, 
u'dfs_datanode_bind_wildcard': None, 
u'dfs_datanode_handler_count': '60', 
u'max_log_backup_index': None, 
u'dfs_thrift_timeout': None, 
u'rm_memory_soft_limit': None, 
u'dfs_datanode_ipc_port': None, 
u'role_config_suppression_datanode_log_dir': None, 
u'com_dssd_flood_conn_client_qdepth': '64', 
u'role_config_suppression_role_triggers': None, 
u'role_config_suppression_datanode_java_heapsize': None, 
u'oom_sigkill_enabled': None, 
u'enable_alerts': None, 
u'DSSDDATANODE_role_env_safety_valve': None, 
u'stacks_collection_directory': None, 
u'rm_io_weight': None, 
u'role_health_suppression_dssd_data_node_pause_duration': None, 
u'dssddatanode_scm_health_enabled': None, 
u'dssddatanode_pause_duration_thresholds': None}

DSSDDATANODE_BASE_CONFIG={
u'dfs_datanode_max_xcievers': None, 
u'stacks_collection_enabled': None, 
u'role_health_suppression_data_node_transceivers_usage': None, 
u'dfs_datanode_drop_cache_behind_reads': None, 
u'stacks_collection_method': None, 
u'dfs_datanode_use_datanode_hostname': None, 
u'datanode_fd_thresholds': None, 
u'unexpected_exits_window': None, 
u'datanode_scm_health_enabled': None,
u'dfs_datanode_drop_cache_behind_writes': None, 
u'datanode_java_heapsize': None, 
u'datanode_log_dir': None, 
u'enable_alerts': None, 
u'role_health_suppression_data_node_web_metric_collection': None, 
u'dfs_datanode_readahead_bytes': None, 
u'dfs_datanode_available_space_balanced_threshold': None, 
u'oom_heap_dump_enabled': None, 
u'datanode_web_metric_collection_thresholds': None, 
u'datanode_data_directories_free_space_percentage_thresholds': None, 
u'datanode_pause_duration_window': None, 
u'datanode_data_directories_free_space_absolute_thresholds': None, 
u'dfs_datanode_data_dir_perm': None, 
u'dfs_balance_bandwidthPerSec': None, 
u'datanode_transceivers_usage_thresholds': None, 
u'role_config_suppression_dfs_data_dir_list': None, 
u'role_health_suppression_data_node_file_descriptor': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'log_directory_free_space_percentage_thresholds': None, 
u'log_event_whitelist': None, 
u'role_config_suppression_datanode_failed_volumes_validator': None, 
u'role_health_suppression_data_node_volume_failures': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'role_health_suppression_datanode_data_directories_free_space': None, 
u'datanode_host_health_enabled': None, 
u'role_config_suppression_datanode_java_opts': None, 
u'max_log_size': None, 
u'role_triggers': None, 
u'datanode_java_opts': None, 
u'role_config_suppression_dfs_datanode_plugins_list': None, 
u'role_health_suppression_data_node_ha_connectivity': None, 
u'hadoop_metrics2_safety_valve': None, 
u'stacks_collection_data_retention': None, 
u'dfs_datanode_http_port': None, 
u'unexpected_exits_thresholds': None, 
u'datanode_free_space_thresholds': None, 
u'role_config_suppression_hadoop_metrics2_safety_valve': None, 
u'dfs_datanode_port': None, 
u'datanode_block_count_thresholds': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'rm_cpu_shares': None, 
u'datanode_volume_failures_thresholds': None, 
u'role_health_suppression_data_node_heap_dump_directory_free_space': None, 
u'log_threshold': None, 
u'role_health_suppression_data_node_scm_health': None, 
u'dfs_datanode_volume_choosing_policy': None, 
u'role_config_suppression_dfs_datanode_data_dir_perm': None, 
u'datanode_pause_duration_thresholds': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'role_config_suppression_datanode_role_env_safety_valve': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'rm_memory_hard_limit': None, 
u'role_health_suppression_data_node_host_health': None, 
u'process_swap_memory_thresholds': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'rlimit_fds': None, 
u'role_config_suppression_datanode_reserved_space_validator': None, 
u'dfs_datanode_du_reserved': None, 
u'dfs_datanode_max_locked_memory': None, 
u'datanode_connectivity_health_enabled': None, 
u'dfs_thrift_threads_min': None, 
u'role_config_suppression_datanode_config_safety_valve': None, 
u'dfs_datanode_https_port': None, 
u'datanode_connectivity_tolerance': None, 
u'dfs_thrift_threads_max': None, 
u'oom_heap_dump_dir': None, 
u'stacks_collection_frequency': None, 
u'role_health_suppression_data_node_free_space_remaining': None, 
u'dfs_datanode_sync_behind_writes': None, 
u'role_health_suppression_data_node_swap_memory_usage': None, 
u'dfs_datanode_plugins_list': None, 
u'dfs_data_dir_list': u'/testdir/dfs/dn', 
u'role_health_suppression_data_node_pause_duration': None, 
u'dfs_datanode_failed_volumes_tolerated': None, 
u'log4j_safety_valve': None, 
u'dfs_datanode_bind_wildcard': None, 
u'dfs_datanode_handler_count': None, 
u'max_log_backup_index': None, 
u'DATANODE_role_env_safety_valve': None, 
u'dfs_thrift_timeout': None, 
u'role_health_suppression_data_node_log_directory_free_space': None, 
u'rm_memory_soft_limit': None, 
u'role_health_suppression_data_node_block_count': None, 
u'dfs_datanode_ipc_port': None, 
u'role_config_suppression_datanode_log_dir': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'role_config_suppression_role_triggers': None, 
u'role_config_suppression_datanode_java_heapsize': None, 
u'oom_sigkill_enabled': None, 
u'enable_config_alerts': None, 
u'datanode_config_safety_valve': None, 
u'stacks_collection_directory': None, 
u'rm_io_weight': None, 
u'dfs_datanode_available_space_balanced_preference': None, 
u'role_health_suppression_data_node_unexpected_exits': None, 
u'datanode_web_metric_collection_enabled': None
}




HDFS_GATEWAY_HOSTS = list(CLUSTER_HOSTS)
HDFS_GATEWAY_HOSTS.append(CM_HOST)
HDFS_GATEWAY_CONFIG = {    
  'dfs_client_use_trash' : 'false',
  #'dfs.client.read.shortcircuit':'true',
  #'dfs.client.read.shortcircuit.skip.checksum':'true',
  #'dfs.client.domain.socket.data.traffic':'false',
  #'dfs.client.use.legacy.blockreader':'false',
  #'dfs.client.use.datanode.hostname':'false'
}



hdfs_HTTPFS_BASE_CONFIG={
u'log_directory_free_space_percentage_thresholds': None, 
u'kerberos_role_princ_name': None, 
u'role_health_suppression_httpfs_scm_health': None, 
u'httpfs_fd_thresholds': None, 
u'httpfs_https_truststore_file': None, 
u'role_health_suppression_httpfs_heap_dump_directory_free_space': None, 
u'role_config_suppression_httpfs_https_keystore_file': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'role_config_suppression_httpfs_log_dir': None, 
u'role_config_suppression_httpfs_process_username': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'role_health_suppression_httpfs_swap_memory_usage': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'stacks_collection_method': None, 
u'httpfs_host_health_enabled': None, 
u'process_swap_memory_thresholds': None, 
u'httpfs_process_groupname': None, 
u'stacks_collection_enabled': None, 
u'role_config_suppression_kerberos_role_princ_name': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'role_triggers': None, 
u'httpfs_scm_health_enabled': None, 
u'httpfs_https_keystore_password': None, 
u'httpfs_https_truststore_password': None, 
u'role_config_suppression_httpfs_process_groupname': None, 
u'role_config_suppression_httpfs_https_truststore_file': None, 
u'role_config_suppression_hdfs_httpfs_signature_secret': None, 
u'role_config_suppression_httpfs_config_safety_valve': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'role_config_suppression_httpfs_java_opts': None, 
u'role_config_suppression_httpfs_https_keystore_password': None, 
u'role_health_suppression_httpfs_unexpected_exits': None, 
u'role_config_suppression_httpfs_role_env_safety_valve': None, 
u'rm_io_weight': None, 
u'stacks_collection_data_retention': None, 
u'rm_memory_hard_limit': None, 
u'httpfs_log_dir': None, 
u'log4j_safety_valve': None, 
u'role_config_suppression_role_triggers': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'rlimit_fds': None, 
u'enable_alerts': None, 
u'httpfs_config_safety_valve': None, 
u'max_log_size': None, 
u'oom_sigkill_enabled': None, 
u'httpfs_java_opts': None, 
u'oom_heap_dump_enabled': None, 
u'unexpected_exits_window': None, 
u'unexpected_exits_thresholds': None, 
u'HTTPFS_role_env_safety_valve': None, 
u'hdfs_httpfs_signature_secret': None, 
u'httpfs_load_balancer': None, 
u'enable_config_alerts': None, 
u'httpfs_https_keystore_file': None,
u'role_config_suppression_stacks_collection_directory': None, 
u'stacks_collection_directory': None, 
u'httpfs_java_heapsize': None, 
u'hdfs_httpfs_admin_port': None, 
u'role_health_suppression_httpfs_file_descriptor': None, 
u'max_log_backup_index': None, 
u'role_config_suppression_httpfs_load_balancer': None, 
u'rm_cpu_shares': None, 
u'hdfs_httpfs_http_port': None, 
u'oom_heap_dump_dir': None, 
u'role_health_suppression_httpfs_host_health': None, 
u'stacks_collection_frequency': None, 
u'role_health_suppression_httpfs_log_directory_free_space': None, 
u'role_config_suppression_httpfs_https_truststore_password': None, 
u'log_threshold': None, 
u'httpfs_use_ssl': None, 
u'rm_memory_soft_limit': None, 
u'httpfs_process_username': None
}



HDFS_FAILOVER_CONTROLLER_BASE_CONFIG={
u'log_directory_free_space_percentage_thresholds': None, 
u'failover_controller_log_dir': None, 
u'log_event_whitelist': None, 
u'rm_io_weight': None, 
u'ha_health_monitor_rpc_timeout_ms': None, 
u'stacks_collection_enabled': None, 
u'fc_config_safety_valve': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'role_health_suppression_hdfs_failovercontroller_unexpected_exits': None, 
u'role_health_suppression_hdfs_failovercontroller_swap_memory_usage': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'role_config_suppression_failovercontroller_role_env_safety_valve': None, 
u'stacks_collection_method': None, 
u'role_health_suppression_hdfs_failovercontroller_heap_dump_directory_free_space': None, 
u'role_config_suppression_failover_controller_log_dir': None, 
u'max_log_size': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'rm_memory_hard_limit': None, 
u'rm_memory_soft_limit': None, 
u'oom_sigkill_enabled': None, 
u'role_config_suppression_fc_config_safety_valve': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'failover_controller_java_heapsize': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'role_health_suppression_hdfs_failovercontroller_log_directory_free_space': None, 
u'process_swap_memory_thresholds': None, 
u'unexpected_exits_window': None, 
u'role_health_suppression_hdfs_failovercontroller_scm_health': None, 
u'stacks_collection_data_retention': None, 
u'role_health_suppression_hdfs_failovercontroller_host_health': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'log4j_safety_valve': None, 
u'role_config_suppression_role_triggers': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'FAILOVERCONTROLLER_role_env_safety_valve': None, 
u'rlimit_fds': None, 
u'role_health_suppression_hdfs_failovercontroller_file_descriptor': None, 
u'enable_alerts': None, 
u'process_auto_restart': None, 
u'role_config_suppression_failover_controller_java_opts': None, 
u'failovercontroller_fd_thresholds': None, 
u'oom_heap_dump_enabled': None, 
u'unexpected_exits_thresholds': None, 
u'role_triggers': None, 
u'failovercontroller_host_health_enabled': None, 
u'failovercontroller_scm_health_enabled': None, 
u'failover_controller_java_opts': None, 
u'stacks_collection_directory': None, 
u'max_log_backup_index': None, 
u'rm_cpu_shares': None, 
u'oom_heap_dump_dir': None, 
u'stacks_collection_frequency': None, 
u'enable_config_alerts': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'log_threshold': None
}

hdfs_BALANCER_BASE_CONFIG={
u'role_config_suppression_balancer_java_opts': None, 
u'balancer_java_opts': None, 
u'log_event_whitelist': None, 
u'balancer_config_safety_valve': None, 
u'rebalancing_policy': None, 
u'rebalancer_threshold': None, 
u'role_config_suppression_balancer_config_safety_valve': None, 
u'enable_config_alerts': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'balancer_java_heapsize': None, 
u'role_config_suppression_cdh_version_validator': None
}

hdfs_JOURNALNODE_BASE_CONFIG={
u'log_directory_free_space_percentage_thresholds': None, 
u'log_event_whitelist': None, 
u'JOURNALNODE_role_env_safety_valve': None, 
u'stacks_collection_enabled': None, 
u'role_health_suppression_journal_node_log_directory_free_space': None, 
u'role_health_suppression_journal_node_fsync_latency': None, 
u'role_config_suppression_journalnode_log_dir': None, 
u'journalnode_java_heapsize': None, 
u'journalnode_bind_wildcard': None, 
u'journalnode_web_metric_collection_enabled': None, 
u'role_health_suppression_journal_node_scm_health': None, 
u'journalnode_web_metric_collection_thresholds': None, 
u'role_health_suppression_journal_node_host_health': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'stacks_collection_method': None, 
u'journalnode_scm_health_enabled': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'rm_memory_hard_limit': None, 
u'role_health_suppression_journal_node_unexpected_exits': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'rm_memory_soft_limit': None, 
u'role_config_suppression_jn_config_safety_valve': None, 
u'dfs_journalnode_rpc_port': None, 
u'dfs_journalnode_edits_dir': None, 
u'role_triggers': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'journalnode_edits_directory_free_space_absolute_thresholds': None, 
u'role_health_suppression_journal_node_swap_memory_usage': None, 
u'journalnode_sync_status_enabled': None, 
u'process_swap_memory_thresholds': None, 
u'unexpected_exits_window': None, 
u'journalnode_host_health_enabled': None, 
u'rm_io_weight': None, 
u'role_config_suppression_journalnode_java_opts': None, 
u'role_health_suppression_journal_node_sync_status': None, 
u'stacks_collection_data_retention': None, 
u'dfs_journalnode_https_port': None, 
u'journalnode_fd_thresholds': None, 
u'role_config_suppression_journalnode_role_env_safety_valve': None, 
u'log4j_safety_valve': None, 
u'role_config_suppression_role_triggers': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'journalnode_fsync_latency_thresholds': None, 
u'jn_config_safety_valve': None, 
u'rlimit_fds': None, 
u'role_config_suppression_dfs_journalnode_edits_dir': None, 
u'role_health_suppression_journal_node_web_metric_collection': None, 
u'enable_alerts': None, 
u'max_log_size': None, 
u'oom_sigkill_enabled': None, 
u'journalnode_gc_duration_thresholds': None, 
u'oom_heap_dump_enabled': None, 
u'role_health_suppression_journal_node_file_descriptor': None, 
u'unexpected_exits_thresholds': None, 
u'journalnode_gc_duration_window': None, 
u'journalnode_edits_directory_free_space_percentage_thresholds': None, 
u'enable_config_alerts': None, 
u'role_health_suppression_journal_node_heap_dump_directory_free_space': None, 
u'journalnode_log_dir': None, 
u'role_health_suppression_journal_node_edits_directory_free_space': None, 
u'journalNode_java_opts': None, 
u'max_log_backup_index': None, 
u'journalnode_sync_status_startup_tolerance': None, 
u'rm_cpu_shares': None, 
u'dfs_journalnode_http_port': None, 
u'oom_heap_dump_dir': None, 
u'stacks_collection_frequency': None, 
u'stacks_collection_directory': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'log_threshold': None, 
u'role_health_suppression_journal_node_gc_duration': None
}

HDFS_NFS_GATEWAY_BASE_CONFIG={
u'log_directory_free_space_percentage_thresholds': None, 
u'role_config_suppression_nfsgateway_role_env_safety_valve': None, 
u'log_event_whitelist': None, 
u'stacks_collection_enabled': None, 
u'role_health_suppression_nfsgateway_scm_health': None, 
u'role_config_suppression_nfsgateway_log_dir': None, 
u'heap_dump_directory_free_space_percentage_thresholds': None, 
u'nfsgateway_fd_thresholds': None, 
u'dfs_nfs3_dump_dir': None, 
u'log_directory_free_space_absolute_thresholds': None, 
u'heap_dump_directory_free_space_absolute_thresholds': None, 
u'nfsgateway_java_heapsize': None, 
u'role_config_suppression_oom_heap_dump_dir': None, 
u'stacks_collection_method': None, 
u'nfsgateway_config_safety_valve': None, 
u'nfs3_portmap_port': None, 
u'nfs3_server_port': None, 
u'nfsgateway_java_opts': None, 
u'process_auto_restart': None, 
u'role_config_suppression_log4j_safety_valve': None, 
u'role_triggers': None, 
u'rm_memory_soft_limit': None, 
u'role_health_suppression_nfsgateway_swap_memory_usage': None, 
u'oom_heap_dump_enabled': None, 
u'role_config_suppression_log_event_whitelist': None, 
u'nfsgateway_host_health_enabled': None, 
u'role_config_suppression_dfs_nfs3_dump_dir': None, 
u'role_config_suppression_cdh_version_validator': None, 
u'rm_memory_hard_limit': None, 
u'dfs_nfs_exports_allowed_hosts': None, 
u'process_swap_memory_thresholds': None, 
u'unexpected_exits_window': None, 
u'rm_io_weight': None, 
u'nfs3_mountd_port': None, 
u'stacks_collection_data_retention': None, 
u'NFSGATEWAY_role_env_safety_valve': None, 
u'log4j_safety_valve': None, 
u'role_config_suppression_role_triggers': None, 
u'role_health_suppression_nfsgateway_host_health': None, 
u'role_health_suppression_nfsgateway_log_directory_free_space': None, 
u'rlimit_fds': None, 
u'enable_alerts': None, 
u'max_log_size': '200M', 
u'oom_sigkill_enabled': None, 
u'role_health_suppression_nfsgateway_file_descriptor': None, 
u'role_config_suppression_dfs_nfs_exports_allowed_hosts': None, 
u'role_health_suppression_nfsgateway_heap_dump_directory_free_space': None, 
u'unexpected_exits_thresholds': None, 
u'role_health_suppression_nfsgateway_dump_directory_free_space': None, 
u'enable_config_alerts': None, 
u'stacks_collection_directory': None, 
u'max_log_backup_index': None, 
u'nfsgateway_dump_directory_free_space_absolute_thresholds': None, 
u'rm_cpu_shares': None, 
u'role_config_suppression_nfsgateway_java_opts': None, 
u'oom_heap_dump_dir': None, 
u'role_health_suppression_nfsgateway_un\
expected_exits': None, 
u'stacks_collection_frequency': None, 
u'role_config_suppression_stacks_collection_directory': None, 
u'log_threshold': None, 
u'role_config_suppression_nfsgateway_config_safety_valve': None, 
u'nfsgateway_dump_directory_free_space_percentage_thresholds': None, 
u'nfsgateway_log_dir': None, 
u'nfsgateway_scm_health_enabled': None
}

#is this httpfs base? 
HDFS_HTTP = {}


YARN_SERVICE_NAME = "YARN"
YARN_SERVICE_CONFIG = {
  'hdfs_service': 'HDFS'
}
YARN_RM_HOST = CM_HOST
YARN_RM_CONFIG = {u'yarn_scheduler_maximum_allocation_mb': u'8192' }
YARN_JHS_HOST = CM_HOST
YARN_JHS_CONFIG = { }
YARN_NM_HOSTS = list(CLUSTER_HOSTS)
YARN_NM_CONFIG = {
  u'yarn_nodemanager_local_dirs': u'/testdir/yarn/nm',
  u'yarn_nodemanager_resource_cpu_vcores': u'32', 
  u'yarn_nodemanager_heartbeat_interval_ms': u'100'
}

YARN_GW_HOSTS = list(CLUSTER_HOSTS)
YARN_GW_CONFIG = {
  u'mapred_submit_replication': u'1',
  u'mapred_reduce_tasks': u'48'
}


HIVE_SERVICE_CONFIG={
  u'hive_metastore_database_port': u'7432', 
  u'hive_metastore_database_password': u'2fzsThuYUA', 
  u'hive_metastore_database_host': u'r2341-d5-us01.dssd.com', 
  u'hive_metastore_database_name': u'hive', 
  u'hive_metastore_database_type': u'postgresql', 
  u'mapreduce_yarn_service': u'YARN'
}


HIVE_SERVICE_NAME = "HIVE"

HIVE_HMS_HOST = CM_HOST
HIVE_HMS_CONFIG = {
  'hive_metastore_java_heapsize': 85306784,
}
HIVE_HS2_HOST = CM_HOST
HIVE_HS2_CONFIG = { }
HIVE_WHC_HOST = CM_HOST
HIVE_WHC_CONFIG = { }
HIVE_GW_HOSTS = list(CLUSTER_HOSTS)
HIVE_GW_CONFIG = { }





IMPALA_SERVICE_NAME = "IMPALA"
IMPALA_SERVICE_CONFIG = {
  'hdfs_service': HDFS_SERVICE_NAME,
  'hive_service': HIVE_SERVICE_NAME,
}

IMPALA_SS_HOST = CM_HOST
IMPALA_SS_CONFIG = { }
IMPALA_CS_HOST = CM_HOST
IMPALA_CS_CONFIG = { }
IMPALA_ID_HOSTS = list(CLUSTER_HOSTS)
IMPALA_ID_CONFIG = { }

IMPALA_SERVICE_NAME = "IMPALA"
IMPALAD={u'scratch_dirs': u'/testdir/impala/impalad', u'impalad_memory_limit': u'86536880128'}



class AfterInitServices(object):
    '''
    '''
    
    def __init__(self):
        '''
        '''

    def deploy_hdfs(self,api,cluster, hdfs_service_name, hdfs_config, hdfs_nn_service_name, hdfs_nn_host, hdfs_nn_config, hdfs_snn_host, hdfs_snn_config, hdfs_dn_hosts, hdfs_dn_config, hdfs_gw_hosts, hdfs_gw_config):

        if api.get_cloudera_manager().get_config().get(u"DSSD_ENABLED"):
            print "deploy_hdfs DSSD_ENABLED!!!!!!!"
            hdfs_service = cluster.create_service(hdfs_service_name, "HDFS")
            hdfs_service.update_config(DSSD_HDFS_SERVICE_CONFIG)
        else:
            print "deploy_hdfs DSSD NOT ENABLED!!!!!!!"
            hdfs_service = cluster.create_service(hdfs_service_name, "HDFS")
            hdfs_service.update_config(hdfs_config)
    #
        nn_role_group = hdfs_service.get_role_config_group("{0}-NAMENODE-BASE".format(hdfs_service_name))
        print "deploy_hdfs nn_role_group:%s", nn_role_group
        nn_role_group.update_config(hdfs_nn_config)
        print "deploy_hdfs hdfs_nn_config uploaded to Clouera manager"
        nn_service_pattern = "{0}-" + hdfs_nn_service_name
        hdfs_service.create_role(nn_service_pattern.format(hdfs_service_name), "NAMENODE", hdfs_nn_host)
   
        snn_role_group = hdfs_service.get_role_config_group("{0}-SECONDARYNAMENODE-BASE".format(hdfs_service_name))
        snn_role_group.update_config(hdfs_snn_config)
        hdfs_service.create_role("{0}-snn".format(hdfs_service_name), "SECONDARYNAMENODE", hdfs_snn_host)


        if api.get_cloudera_manager().get_config().get(u'DSSD_ENABLED'):
            print "deploy_hdfs DSSD enabled, getting dn_role_group"
            dn_role_group = hdfs_service.get_role_config_group("{0}-DSSDDATANODE-BASE".format(hdfs_service_name))
            print "deploy_hdfs dn_role_group:", dn_role_group
            dn_role_group.update_config(DSSD_DATANODE_CONFIG)
            print "deploy_hdfs updating dn_role_group.config"
        else:
            dn_role_group = hdfs_service.get_role_config_group("{0}-DATANODE-BASE".format(hdfs_service_name))
            dn_role_group.update_config(hdfs_dn_config)
   
        gw_role_group = hdfs_service.get_role_config_group("{0}-GATEWAY-BASE".format(hdfs_service_name))
        gw_role_group.update_config(hdfs_gw_config)
   
        datanode = 0
        for host in hdfs_dn_hosts:
            datanode += 1
            hdfs_service.create_role("{0}-dn-".format(hdfs_service_name) + str(datanode), "DSSDDATANODE", host)
   
        gateway = 0
        for host in hdfs_gw_hosts:
            gateway += 1
            hdfs_service.create_role("{0}-gw-".format(hdfs_service_name) + str(gateway), "GATEWAY", host)
   
        return hdfs_service



# Deploys Impala - statestore, catalogserver, impalads
    def deploy_impala(self,cluster, impala_service_name, impala_service_config, impala_ss_host, impala_ss_config, impala_cs_host, impala_cs_config, impala_id_hosts, impala_id_config):
        impala_service = cluster.create_service(impala_service_name, "IMPALA")
        impala_service.update_config(impala_service_config)
   
        ss = impala_service.get_role_config_group("{0}-STATESTORE-BASE".format(impala_service_name))
        ss.update_config(impala_ss_config)
        impala_service.create_role("{0}-ss".format(impala_service_name), "STATESTORE", impala_ss_host)
   
        cs = impala_service.get_role_config_group("{0}-CATALOGSERVER-BASE".format(impala_service_name))
        cs.update_config(impala_cs_config)
        impala_service.create_role("{0}-cs".format(impala_service_name), "CATALOGSERVER", impala_cs_host)
   
        id = impala_service.get_role_config_group("{0}-IMPALAD-BASE".format(impala_service_name))
        id.update_config(impala_id_config)
   
        impalad = 0
        for host in impala_id_hosts:
            impalad += 1
            impala_service.create_role("{0}-id-".format(impala_service_name) + str(impalad), "IMPALAD", host)

        # Don't think we need these at the end:
        #impala_service.create_impala_catalog_database()
        #impala_service.create_impala_catalog_database_tables()
        #impala_service.create_impala_user_dir()
   
        return impala_service
   
   

    def deploy_hive(self,cluster, hive_service_name, hive_service_config, hive_hms_host, hive_hms_config, hive_hs2_host, hive_hs2_config, hive_whc_host, hive_whc_config, hive_gw_hosts, hive_gw_config):
        hive_service = cluster.create_service(hive_service_name, "HIVE")
        hive_service.update_config(hive_service_config)
   
        hms = hive_service.get_role_config_group("{0}-HIVEMETASTORE-BASE".format(hive_service_name))
        hms.update_config(hive_hms_config)
        hive_service.create_role("{0}-hms".format(hive_service_name), "HIVEMETASTORE", hive_hms_host)
   
        hs2 = hive_service.get_role_config_group("{0}-HIVESERVER2-BASE".format(hive_service_name))
        hs2.update_config(hive_hs2_config)
        hive_service.create_role("{0}-hs2".format(hive_service_name), "HIVESERVER2", hive_hs2_host)
   
        whc = hive_service.get_role_config_group("{0}-WEBHCAT-BASE".format(hive_service_name))
        whc.update_config(hive_whc_config)
        hive_service.create_role("{0}-whc".format(hive_service_name), "WEBHCAT", hive_whc_host)
   
        gw = hive_service.get_role_config_group("{0}-GATEWAY-BASE".format(hive_service_name))
        gw.update_config(hive_gw_config)
   
        gateway = 0
        for host in hive_gw_hosts:
            gateway += 1
            hive_service.create_role("{0}-gw-".format(hive_service_name) + str(gateway), "GATEWAY", host)
   
        return hive_service



    def deploy_yarn(self,cluster, yarn_service_name, yarn_service_config, yarn_rm_host, yarn_rm_config, yarn_jhs_host, yarn_jhs_config, yarn_nm_hosts, yarn_nm_config, yarn_gw_hosts, yarn_gw_config):
        yarn_service = cluster.create_service(yarn_service_name, "YARN")
        yarn_service.update_config(yarn_service_config)
      
        rm = yarn_service.get_role_config_group("{0}-RESOURCEMANAGER-BASE".format(yarn_service_name))
        rm.update_config(yarn_rm_config)
        yarn_service.create_role("{0}-rm".format(yarn_service_name), "RESOURCEMANAGER", yarn_rm_host)
      
        jhs = yarn_service.get_role_config_group("{0}-JOBHISTORY-BASE".format(yarn_service_name))
        jhs.update_config(yarn_jhs_config)
        yarn_service.create_role("{0}-jhs".format(yarn_service_name), "JOBHISTORY", yarn_jhs_host)
   
        nm = yarn_service.get_role_config_group("{0}-NODEMANAGER-BASE".format(yarn_service_name))
        nm.update_config(yarn_nm_config)
   
        nodemanager = 0
        for host in yarn_nm_hosts:
            nodemanager += 1
            yarn_service.create_role("{0}-nm-".format(yarn_service_name) + str(nodemanager), "NODEMANAGER", host)
   
        gw = yarn_service.get_role_config_group("{0}-GATEWAY-BASE".format(yarn_service_name))
        gw.update_config(yarn_gw_config)
   
        gateway = 0
        for host in yarn_gw_hosts:
            gateway += 1
            yarn_service.create_role("{0}-gw-".format(yarn_service_name) + str(gateway), "GATEWAY", host)
   
        #TODO need api version 6 for these, but I think they are done automatically?
        #yarn_service.create_yarn_job_history_dir()
        #yarn_service.create_yarn_node_manager_remote_app_log_dir()
   
        return yarn_service



  


    def init_hdfs(self,hdfs_service, hdfs_name):
        print "init_hdfs, make sure cleandatanode.sh is run first to clean the NN and DN storage"
        cmd = hdfs_service.format_hdfs("{0}-nn".format(hdfs_name))[0]
        if not cmd.wait(60).success:
            print "WARNING: Failed to format HDFS, exiting, fix before continuing"
            exit(0) 
        hdfs_service.start().wait()


    def init_hive(self,hive_service):
        hive_service.create_hive_metastore_database()
        hive_service.create_hive_metastore_tables()
        hive_service.create_hive_warehouse()
    #don't think that the create_hive_userdir call is needed as the create_hive_warehouse already creates it
    #hive_service.create_hive_userdir()



    def test(self):
        print "parcels downloaded, verify you can see the services in add services"
        print "and parcels are activated for CDH, "
        api = ApiResource('r2341-d5-us01', username='admin', password='admin')
        #we need to revisit the host inspect
        #inspect_hosts(api)
        CLUSTER = api.get_all_clusters()[0] 
        print "CLUSTER:%s,", CLUSTER
  
        if api.get_cloudera_manager().get_config().get(u"DSSD_ENABLED"):
            print "deploying DSSD hdfs"
            hdfs_service = self.deploy_hdfs(api,CLUSTER, HDFS_SERVICE_NAME, HDFS_SERVICE_CONFIG, HDFS_NAMENODE_SERVICE_NAME, HDFS_NAMENODE_HOST, HDFS_NAMENODE_CONFIG, HDFS_SECONDARY_NAMENODE_HOST, HDFS_SECONDARY_NAMENODE_CONFIG, HDFS_DATANODE_HOSTS, DSSD_DATANODE_CONFIG, HDFS_GATEWAY_HOSTS, HDFS_GATEWAY_CONFIG)
        else:
            print "deploying non-dssd hdfs"
            hdfs_service = self.deploy_hdfs(api,CLUSTER, HDFS_SERVICE_NAME, HDFS_SERVICE_CONFIG, HDFS_NAMENODE_SERVICE_NAME, HDFS_NAMENODE_HOST, HDFS_NAMENODE_CONFIG, HDFS_SECONDARY_NAMENODE_HOST, HDFS_SECONDARY_NAMENODE_CONFIG, HDFS_DATANODE_HOSTS, HDFS_DATANODE_CONFIG, HDFS_GATEWAY_HOSTS, HDFS_GATEWAY_CONFIG)
  
        print "Deployed HDFS service " + HDFS_SERVICE_NAME + " using NameNode on " + HDFS_NAMENODE_HOST + ", SecondaryNameNode on " + HDFS_SECONDARY_NAMENODE_HOST + ", and DataNodes running on: "
        #PRETTY_PRINT.pprint(HDFS_DATANODE_HOSTS)
        self.init_hdfs(hdfs_service, HDFS_SERVICE_NAME)
        print "formatted namenode in hdfs service"
        CLUSTER.deploy_client_config()
  
  

        print 'installing yarn'
        yarn_service = self.deploy_yarn(CLUSTER, YARN_SERVICE_NAME, YARN_SERVICE_CONFIG, YARN_RM_HOST, YARN_RM_CONFIG, YARN_JHS_HOST, YARN_JHS_CONFIG, YARN_NM_HOSTS, YARN_NM_CONFIG, YARN_GW_HOSTS, YARN_GW_CONFIG)
        print "Deployed YARN service " + YARN_SERVICE_NAME + " using ResourceManager on " + YARN_RM_HOST + ", JobHistoryServer on " + YARN_JHS_HOST + ", and NodeManagers on "
        #PRETTY_PRINT.pprint(YARN_NM_HOSTS)
        yarn_service.start().wait()
        CLUSTER.deploy_client_config()


        print "deploying hive"
        hive_service = self.deploy_hive(CLUSTER, HIVE_SERVICE_NAME, HIVE_SERVICE_CONFIG, HIVE_HMS_HOST, HIVE_HMS_CONFIG, HIVE_HS2_HOST, HIVE_HS2_CONFIG, HIVE_WHC_HOST, HIVE_WHC_CONFIG, HIVE_GW_HOSTS, HIVE_GW_CONFIG)
        print "Depoyed Hive service " + HIVE_SERVICE_NAME + " using HiveMetastoreServer on " + HIVE_HMS_HOST + " and HiveServer2 on " + HIVE_HS2_HOST
        hive_service.start().wait()
        self.init_hive(hive_service)
        print "Initialized Hive service"
        CLUSTER.deploy_client_config()


        impala_service = self.deploy_impala(CLUSTER, IMPALA_SERVICE_NAME, IMPALA_SERVICE_CONFIG, IMPALA_SS_HOST, IMPALA_SS_CONFIG, IMPALA_CS_HOST, IMPALA_CS_CONFIG, IMPALA_ID_HOSTS, IMPALA_ID_CONFIG)
        print "Deployed Impala service " + IMPALA_SERVICE_NAME + " using StateStore on " + IMPALA_SS_HOST + ", CatalogServer on " + IMPALA_CS_HOST + ", and ImpalaDaemons on "
        #PRETTY_PRINT.pprint(IMPALA_ID_HOSTS)
        impala_service.start().wait()
        CLUSTER.deploy_client_config()

