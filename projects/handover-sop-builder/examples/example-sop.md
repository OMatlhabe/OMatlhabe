# Weekly Supplier Payment Run: Handover SOP (fictional example)

This example uses a made-up process and made-up roles to show the output style. It is abridged.

## 1. Document control

| Field | Value |
| --- | --- |
| Process | Weekly supplier payment run |
| Owner | Accounts Payable Lead |
| Backup | Finance Operations Analyst |
| Version | 0.4 draft |
| Last verified | [TO CONFIRM: not yet verified by backup] |
| Review cadence | Quarterly |

## 2. TL;DR

Every Thursday by 15:00 UK time, approved supplier invoices are batched and sent to the bank for payment on Friday.

- **Biggest risk:** invoices approved after the 12:00 cut-off are missed and suppliers chase by email.
- **Start here:** Section 8, Procedure A.
- **Still open:** bank approver cover when the Finance Director is away (Section 15).

## 6. Systems and access

| System | Used for | Permission needed | How to get it |
| --- | --- | --- | --- |
| Accounting system | Export approved invoices | "Payments Preparer" role | Request from the IT service desk with manager approval; usually same day |
| Bank portal | Upload and release the batch | Preparer on one login, Approver on another | Finance Director grants Approver; Preparer is granted by the bank administrator |

## 8. Procedure A: prepare and submit the batch

1. **Export approved invoices.** In the accounting system open Payables, then Approved, set the date range to last Friday through today at 12:00, and export to CSV. *Expected:* a file named `approved_YYYYMMDD.csv` with one row per invoice. *If the file is empty:* see Section 12, row 1.
2. **Check totals.** Compare the CSV total with the "Approved, unpaid" figure on the Payables dashboard. *Expected:* they match to the penny. *If not:* do not continue; see Section 12, row 2.
3. **Upload to the bank portal.** Bank portal, then Payments, then Import batch, then choose the CSV. *Expected:* a preview showing the same count and total.
4. **Request approval.** Click Submit for approval and message the approver role in the finance channel with the batch total. *Expected:* status changes to "Awaiting approval".
5. **Confirm release.** After the approver releases it, save a screenshot of the confirmation in the weekly folder.

## 12. Troubleshooting

| Symptom | Likely cause | Fix | Escalate to |
| --- | --- | --- | --- |
| Export is empty | Date range or role filter reset | Re-apply date range; confirm you hold the Payments Preparer role | IT service desk |
| Totals differ | An invoice approved after export, or a partially approved invoice | Re-export; list invoices missing from the CSV | Accounts Payable Lead |
| Bank rejects a row | Supplier bank details changed | Hold that invoice, verify details by phone using the supplier's known number, then resubmit | Finance Director |
| Approver unavailable | Leave or travel | Use the delegate approver [TO CONFIRM: named delegate] | Finance Director |

## 15. Open items

| # | Item | Owner | Blocks execution? |
| --- | --- | --- | --- |
| 1 | Name the delegate approver | Finance Director | Yes, when the approver is away |
| 2 | Add screenshots of the bank portal import screen | Accounts Payable Lead | No |
