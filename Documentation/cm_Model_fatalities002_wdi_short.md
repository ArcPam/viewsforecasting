| Model                   | Included variable name      | Database variable name        | Transformations                                                                                                                                  |
|:------------------------|:----------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| fatalities002_wdi_short | ln_ged_sb_dep               | ged2_cm.ged_sb_best_sum_nokgi | ['missing.fill()', 'ops.ln()']                                                                                                                   |
| fatalities002_wdi_short | ln_ged_sb                   | ged2_cm.ged_sb_best_sum_nokgi | ['missing.fill()', 'ops.ln()']                                                                                                                   |
| fatalities002_wdi_short | decay_ged_sb_5              | ged2_cm.ged_sb_best_sum_nokgi | ['missing.replace_na()', 'temporal.decay(24)', 'temporal.time_since()', 'bool.gte(5)', 'missing.replace_na()']                                   |
| fatalities002_wdi_short | decay_ged_os_5              | ged2_cm.ged_os_best_sum_nokgi | ['missing.replace_na()', 'temporal.decay(24)', 'temporal.time_since()', 'bool.gte(5)', 'missing.replace_na()']                                   |
| fatalities002_wdi_short | splag_1_decay_ged_sb_5      | ged2_cm.ged_sb_best_sum_nokgi | ['missing.replace_na()', 'spatial.countrylag(1, 1, 0, 0)', 'temporal.decay(24)', 'temporal.time_since()', 'bool.gte(5)', 'missing.replace_na()'] |
| fatalities002_wdi_short | wdi_sp_pop_totl             | wdi_cy.wdi_sp_pop_totl        | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_ag_lnd_frst_k2          | wdi_cy.wdi_ag_lnd_frst_k2     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_dt_oda_odat_pc_zs       | wdi_cy.wdi_dt_oda_odat_pc_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_ms_mil_xpnd_gd_zs       | wdi_cy.wdi_ms_mil_xpnd_gd_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_ms_mil_xpnd_zs          | wdi_cy.wdi_ms_mil_xpnd_zs     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_nv_agr_totl_kd          | wdi_cy.wdi_nv_agr_totl_kd     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_nv_agr_totl_kn          | wdi_cy.wdi_nv_agr_totl_kn     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_ny_gdp_pcap_kd          | wdi_cy.wdi_ny_gdp_pcap_kd     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_dyn_le00_in          | wdi_cy.wdi_sp_dyn_le00_in     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_se_enr_prim_fm_zs       | wdi_cy.wdi_se_enr_prim_fm_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_se_enr_prsc_fm_zs       | wdi_cy.wdi_se_enr_prsc_fm_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_se_prm_nenr             | wdi_cy.wdi_se_prm_nenr        | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sh_sta_maln_zs          | wdi_cy.wdi_sh_sta_maln_zs     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sh_sta_stnt_zs          | wdi_cy.wdi_sh_sta_stnt_zs     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sl_tlf_totl_fe_zs       | wdi_cy.wdi_sl_tlf_totl_fe_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sm_pop_refg_or          | wdi_cy.wdi_sm_pop_refg_or     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sm_pop_netm             | wdi_cy.wdi_sm_pop_netm        | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sm_pop_totl_zs          | wdi_cy.wdi_sm_pop_totl_zs     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_dyn_imrt_in          | wdi_cy.wdi_sp_dyn_imrt_in     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sh_dyn_mort_fe          | wdi_cy.wdi_sh_dyn_mort_fe     | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_pop_0014_fe_zs       | wdi_cy.wdi_sp_pop_0014_fe_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_pop_1564_fe_zs       | wdi_cy.wdi_sp_pop_1564_fe_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_pop_65up_fe_zs       | wdi_cy.wdi_sp_pop_65up_fe_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_pop_grow             | wdi_cy.wdi_sp_pop_grow        | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | wdi_sp_urb_totl_in_zs       | wdi_cy.wdi_sp_urb_totl_in_zs  | ['missing.fill()', 'temporal.tlag(12)', 'missing.fill()']                                                                                        |
| fatalities002_wdi_short | splag_wdi_sl_tlf_totl_fe_zs | wdi_cy.wdi_sl_tlf_totl_fe_zs  | ['missing.replace_na()', 'spatial.countrylag(1, 1, 0, 0)', 'temporal.tlag(12)', 'missing.fill()']                                                |
| fatalities002_wdi_short | splag_wdi_sm_pop_refg_or    | wdi_cy.wdi_sm_pop_refg_or     | ['missing.replace_na()', 'spatial.countrylag(1, 1, 0, 0)', 'temporal.tlag(12)', 'missing.fill()']                                                |
| fatalities002_wdi_short | splag_wdi_sm_pop_netm       | wdi_cy.wdi_sm_pop_netm        | ['missing.replace_na()', 'spatial.countrylag(1, 1, 0, 0)', 'temporal.tlag(12)', 'missing.fill()']                                                |
| fatalities002_wdi_short | splag_wdi_ag_lnd_frst_k2    | wdi_cy.wdi_ag_lnd_frst_k2     | ['missing.replace_na()', 'spatial.countrylag(1, 1, 0, 0)', 'temporal.tlag(12)', 'missing.fill()']                                                |