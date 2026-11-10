---
description: Fix Keymaster, entitlement and escrow errors when a script won't start.
---

# Escrow errors

Our scripts are escrowed by Cfx.re. The protected files only run on a server whose **license key belongs to the Cfx.re account that owns the script**.

<details>

<summary><code>You lack the required entitlement to use ...</code></summary>

The server's license key comes from a different Cfx.re account than the one that bought the script.

* Make the license key (`sv_licenseKey` in `server.cfg`) on the **same account** that has the script in Keymaster → Granted Assets.
* Restart the whole server after changing the key.

</details>

<details>

<summary><code>Failed to verify protected resource</code> or a syntax error in an escrowed file</summary>

The encrypted files were changed or damaged.

* Download the script again from Keymaster and replace the whole folder.
* Upload with FTP in **binary** mode (not ASCII or "auto").
* Don't open and save escrowed files in an editor. Only the open files (`config.lua`, `bridge/`, `locales/` and similar) can be edited.

</details>

<details>

<summary>The script doesn't start after renaming the folder</summary>

Put the original folder name back. Escrowed scripts must keep the name they were downloaded with.

</details>

<details>

<summary>It worked before and broke after a server update or artifact change</summary>

* Use a recent **recommended** server artifact. Very old artifacts can't load newer escrowed files.
* Make sure you're on the latest version of the script (Keymaster → Granted Assets).

</details>

Still stuck? Open a ticket in the [Huncho World Discord](https://discord.gg/hP8VTtwgs5) with your console output.
