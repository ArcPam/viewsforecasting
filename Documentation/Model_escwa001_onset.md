| Model          | Included variable name        | Database variable name                | Transformations                                                                                                 |
|:---------------|:------------------------------|:--------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| escwa001_onset | 'ged_sb_onset24'              | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.onset'", "'bool.gte'", "'missing.replace_na'"]                              |
| escwa001_onset | 'decay_12_ged_sb_1'           | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_12_ged_ns_1'           | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_12_ged_os_1'           | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_ged_sb_100'            | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_ged_ns_100'            | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_ged_os_100'            | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_ged_sb_500'            | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_ged_ns_500'            | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'decay_ged_os_500'            | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.decay'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]     |
| escwa001_onset | 'ts_ged_sb_1'                 | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_ns_1'                 | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_os_1'                 | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_sb_100'               | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_ns_100'               | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_os_100'               | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_sb_500'               | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_ns_500'               | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'ts_ged_os_500'               | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"]                         |
| escwa001_onset | 'splag_1_decay_ged_sb_100'    | 'ged2_cm.ged_sb_best_sum_nokgi'       | ["'missing.replace_na'", "'spatial.countrylag'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"] |
| escwa001_onset | 'splag_1_decay_ged_ns_100'    | 'ged2_cm.ged_ns_best_sum_nokgi'       | ["'missing.replace_na'", "'spatial.countrylag'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"] |
| escwa001_onset | 'splag_1_decay_ged_os_100'    | 'ged2_cm.ged_os_best_sum_nokgi'       | ["'missing.replace_na'", "'spatial.countrylag'", "'temporal.time_since'", "'bool.gte'", "'missing.replace_na'"] |
| escwa001_onset | 'wfpmp_mp_price'              | 'wfpmp_cm.wfpmp_mp_price'             | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'wfpmp_wheat_price'           | 'wfpmp_cm.wfpmp_wheat_price'          | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'wfpmp_sugar_price'           | 'wfpmp_cm.wfpmp_sugar_price'          | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'wfpmp_milk_price'            | 'wfpmp_cm.wfpmp_milk_price'           | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'wfpmp_meat_price'            | 'wfpmp_cm.wfpmp_meat_price'           | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'wfpmp_mp_price_t12'          | 'wfpmp_cm.wfpmp_mp_price'             | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wfpmp_wheat_price_t12'       | 'wfpmp_cm.wfpmp_wheat_price'          | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wfpmp_sugar_price_t12'       | 'wfpmp_cm.wfpmp_sugar_price'          | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wfpmp_milk_price_t12'        | 'wfpmp_cm.wfpmp_milk_price'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wfpmp_meat_price_t12'        | 'wfpmp_cm.wfpmp_meat_price'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'imfweo_ngdp_rpch_tcurrent'   | 'imfweo_cm.ngdp_rpch_tcurrent'        | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'imfweo_ngdp_rpch_tmin1'      | 'imfweo_cm.ngdp_rpch_tmin1'           | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'imfweo_ngdp_rpch_tplus1'     | 'imfweo_cm.ngdp_rpch_tplus1'          | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'imfweo_ngdp_rpch_tplus2'     | 'imfweo_cm.ngdp_rpch_tplus2'          | ["'missing.replace_na'"]                                                                                        |
| escwa001_onset | 'agr_withdrawal_pct_t48'      | 'fao_aqua_cy.agr_withdrawal_pct'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'dam_cap_pcap_t48'            | 'fao_aqua_cy.dam_cap_pcap'            | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'groundwater_export_t48'      | 'fao_aqua_cy.groundwater_export'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'fresh_withdrawal_pct_t48'    | 'fao_aqua_cy.fresh_withdrawal_pct'    | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'ind_efficiency_48'           | 'fao_aqua_cy.ind_efficiency'          | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'irr_agr_efficiency_48'       | 'fao_aqua_cy.irr_agr_efficiency'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'services_efficiency_48'      | 'fao_aqua_cy.services_efficiency'     | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'general_efficiency_t48'      | 'fao_aqua_cy.general_efficiency'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'water_stress_t48'            | 'fao_aqua_cy.water_stress'            | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'renewable_internal_pcap_t48' | 'fao_aqua_cy.renewable_internal_pcap' | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'renewable_pcap_t48'          | 'fao_aqua_cy.renewable_pcap'          | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2x_clphy'              | 'vdem_v12_cy.vdem_v12_v2x_clphy'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2xcl_dmove'            | 'vdem_v12_cy.vdem_v12_v2xcl_dmove'    | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2xcl_rol'              | 'vdem_v12_cy.vdem_v12_v2xcl_rol'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2x_civlib'             | 'vdem_v12_cy.vdem_v12_v2x_civlib'     | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2xel_regelec'          | 'vdem_v12_cy.vdem_v12_v2xel_regelec'  | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2xcl_acjst'            | 'vdem_v12_cy.vdem_v12_v2xcl_acjst'    | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2x_gencl'              | 'vdem_v12_cy.vdem_v12_v2x_gencl'      | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2xeg_eqdr'             | 'vdem_v12_cy.vdem_v12_v2xeg_eqdr'     | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2x_egal'               | 'vdem_v12_cy.vdem_v12_v2x_egal'       | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'vdem_v2x_clpriv'             | 'vdem_v12_cy.vdem_v12_v2x_clpriv'     | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_sm_pop_refg_or'          | 'wdi_cy.wdi_sm_pop_refg_or'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_sp_pop_totl'             | 'wdi_cy.wdi_sp_pop_totl'              | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_sm_pop_netm'             | 'wdi_cy.wdi_sm_pop_netm'              | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_sl_uem_advn_zs'          | 'wdi_cy.wdi_sl_uem_advn_zs'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_nv_agr_totl_kn'          | 'wdi_cy.wdi_nv_agr_totl_kn'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_sp_hou_fema_zs'          | 'wdi_health_cy.wdi_sp_hou_fema_zs'    | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_ag_lnd_totl_ru_k2'       | 'wdi_cy.wdi_ag_lnd_totl_ru_k2'        | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_nv_agr_totl_kd'          | 'wdi_cy.wdi_nv_agr_totl_kd'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_nv_agr_totl_cn'          | 'wdi_cy.wdi_nv_agr_totl_cn'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_sh_sta_maln_zs'          | 'wdi_cy.wdi_sh_sta_maln_zs'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |
| escwa001_onset | 'wdi_ny_gdp_pcap_kd'          | 'wdi_cy.wdi_ny_gdp_pcap_kd'           | ["'missing.fill'", "'temporal.tlag'", "'missing.fill'"]                                                         |