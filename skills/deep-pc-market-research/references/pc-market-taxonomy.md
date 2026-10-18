# PC Market Taxonomy

Use this taxonomy to decompose broad PC market questions into searchable lanes and actionable factors.

## Scope Vocabulary

- PC: laptops, desktops, workstations, commercial PCs, consumer PCs, gaming PCs, education PCs, and AI PCs.
- AI PC: PCs with local AI acceleration or platform claims around NPU, Copilot+ PC, local model inference, or AI-enabled user workflows.
- Time horizon:
  - near-term: current quarter to 6 months
  - medium-term: 6-18 months
  - long-term: 18 months or more
- Market effect:
  - shipment volume
  - average selling price
  - product mix
  - gross margin
  - vendor market share
  - inventory
  - replacement cycle

## Demand

Typical factors:

- Windows 10 end-of-support and Windows 11 migration.
- Enterprise refresh cycles and commercial notebook replacement.
- Pandemic-era installed base aging into replacement windows.
- Consumer confidence and discretionary spending.
- Education procurement cycles.
- Gaming laptop demand.
- Remote or hybrid work demand.
- AI PC as a premium replacement trigger.

Useful queries:

- `PC shipment forecast enterprise refresh Windows 10 end of support`
- `commercial PC replacement cycle 2026 Windows 11 migration`
- `AI PC enterprise adoption refresh cycle forecast`
- `consumer PC demand recovery laptop shipments`

## Supply

Typical factors:

- OEM and ODM inventory normalization.
- CPU, GPU, and NPU platform availability.
- Notebook ODM shipment trends.
- Logistics disruptions.
- Regional supply-chain relocation.
- Component lead times.

Useful queries:

- `notebook ODM shipments inventory PC market`
- `PC OEM inventory normalization shipment forecast`
- `CPU supply constraints PC OEM notebook`
- `supply chain disruption PC market laptops`

## Cost

Typical factors:

- DRAM price trends.
- NAND and SSD price trends.
- Display panel pricing.
- Battery and power component costs.
- CPU, GPU, and NPU bill-of-material changes.
- Exchange rates, tariffs, and freight costs.

Cost factors may affect ASP, margin, promotion intensity, or mix even when shipments do not move directly.

Useful queries:

- `DRAM price trend impact PC OEM margins`
- `NAND SSD price PC notebook market`
- `notebook panel price trend PC market`
- `tariff impact PC market laptops`

## Technology

Typical factors:

- AI PC and Copilot+ PC adoption.
- NPU performance and local inference use cases.
- ARM PC versus x86 platform competition.
- Windows ecosystem readiness.
- Battery life improvements.
- Enterprise AI application maturity.

Avoid generic factors such as "AI PC is growing." Convert them into testable drivers:

- shipment forecast
- attach rate
- enterprise procurement evidence
- ASP uplift
- software use case readiness
- silicon platform availability

Useful queries:

- `AI PC shipment forecast IDC Gartner Canalys`
- `Copilot+ PC adoption enterprise forecast`
- `NPU AI PC local inference enterprise use cases`
- `ARM PC market share Windows laptops`

## Competition

Typical factors:

- Lenovo, HP, Dell, Apple, ASUS, Acer share changes.
- Vendor earnings commentary on PC demand.
- Commercial account wins or losses.
- Channel pricing and promotion strategy.
- Apple Mac demand and refresh timing.
- Regional brand competition.

Useful queries:

- `Lenovo HP Dell PC market share 2026`
- `PC vendor earnings call commercial demand notebook`
- `Apple Mac shipments PC market share`
- `Canalys PC market share Lenovo HP Dell`

## Macro

Typical factors:

- Interest rates and financing conditions.
- Inflation and consumer purchasing power.
- Enterprise IT budget and capex.
- Currency movements.
- Unemployment and consumer sentiment.
- Government stimulus, procurement, or restrictions.
- Geopolitical risk and tariffs.

Always state the transmission path:

```text
macro variable -> buyer budget or supply cost -> PC purchase timing, ASP, margin, or inventory
```

Useful queries:

- `enterprise IT budget outlook PC refresh`
- `consumer confidence PC demand laptops`
- `currency impact PC OEM margins`
- `tariff policy impact personal computers`

## Channel

Typical factors:

- Retail sell-through.
- Distributor inventory.
- E-commerce promotion events.
- Commercial channel orders.
- Education and government tenders.
- Regional price competition.

Useful queries:

- `PC channel inventory sell through notebook market`
- `retail PC sales promotion laptop demand`
- `commercial PC channel orders`
- `education PC procurement market`

## Policy And Lifecycle

Typical factors:

- Windows 10 support ending.
- Public-sector procurement rules.
- Security or compliance requirements.
- Domestic substitution and trusted computing programs.
- Device lifecycle aging.

Useful queries:

- `Windows 10 end of support PC refresh cycle`
- `government PC procurement policy market`
- `commercial PC lifecycle replacement cycle`
- `China domestic PC procurement policy`

## Aggregation Guidance

Merge claims into one factor when they describe the same mechanism. For example:

- "Windows 10 EOL drives refresh"
- "Windows migration increases commercial PC replacement"
- "enterprise installed base upgrade cycle"

These should become one factor about commercial refresh demand, with multiple evidence items and caveats.
