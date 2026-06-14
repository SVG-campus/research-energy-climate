# Preregistration — `research-energy-climate`
 
**Pillar:** `research-energy-climate`  
**Title:** Weather-to-Demand Causal Mapping (ECT-2026-002)
**Date:** 2026-06-14  
**ORCID Identifier:** `0009-0004-9601-5617`

## Charter (one paragraph)

Link techno-economic and weather/climate signals under explicit uncertainty and caps. This study investigates the causal direction flowing from local temperature anomalies and degree day indices to next-day electricity load deviations, while validating that O-Information correctly identifies these overlapping weather factors as redundant causal drivers.

## Primary question (Layer A)

- **Question:** Do temperature metrics (temperature_2m, temperature_max_2m) and degree day proxies (heating_degree_proxy, cooling_degree_proxy) causally drive next-day load deviation from the 14-day rolling mean?
- **Expected DAG:**
  $$\text{Temperature} \rightarrow \text{Degree Days} \rightarrow \text{Weather Stress} \rightarrow \text{Next-Day Load Outcome}$$
  No reverse causality allowed (no directed edges from next-day load outcome to weather variables).
- **O-Info State:** Redundancy ($I_O > 0$, since overlapping temperature variables share mutual information about load deviations).
- **Primary metric:** Discovered directed edges from weather to load deviation and the Information Coefficient of nonlinear weather stress interactions.
- **Direction / threshold:** $\alpha = 0.05$ for PC algorithm skeleton search. Discovered weather-to-load directed edges must be $\ge 1$. The predictive top-bottom spread must exceed the p95 Spectral MC null distribution ($p < 0.05$).

## Null / negative controls

- **Null model:** Phase-shuffled Spectral Monte Carlo (FFT surrogate paths preserving load autocorrelation structure).
- **Caps:** Capped at $N = 25$ runs for local smokes (`runs/smoke.yaml`); $N = 1000$ for full remote promotion validation with run ID `charter_energy_demand_prereg_run_01`.

## Truth scope & ethics

- **Scope:** Observational daily grid load data. This serves as a physical causal baseline model under the **ECT-2026** standard.
- **Data rights:** Utilizes NYISO and Open-Meteo weather records pinned in `datasets.yaml`.

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact. Follow the meta checklist [PROMOTION_CHECKLIST.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) before editing canonical summaries.
