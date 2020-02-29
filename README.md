Various tools I've made for bug bounty hunting

<details>
<summary>/js</summary>
<ul>
  <li>
    <b>beautify-js.py:</b>
    <ul>
      <li>Why: Mass download of JS files and beautify for easier reading/grepping</li>
      <li>Uses: Recon, Source code</li>
      <li>Syntax: <code>python3 beautify-js.py --infile [file with a ton of URLS in it] --outdir [where to save the beautified results]</code></li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary>/ssrf</summary>
<ul>
  <li>
    <b>sentry-scraping-ssrf.py:</b> 
    <ul>
      <li>Why: Sentry scraping could result in unwanted exposure of debug info</li> 
      <li>Uses: SSRF</li>
      <li> Syntax: <code>python3 sentry-scraping-ssrf.py --infile [file with a ton of URLS in it] --payload [a malicious callback link (burp collab?) --threads [x]</code></li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary>/generators</summary>
<ul>
  <li>
    <b>wayback-words.py:</b> 
    <ul>
      <li>Why: Generate a wordlist based on things from the past</li>
      <li>Uses: Recon</li>
      <li>Syntax: <code>python3 wayback-words.py --infile [file with a ton of URLs in it] --outfile [where to save the generated list] --exclusions [extensions to exclude (ie: .png .jpg)]</code></li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary>/fuzzing</summary>
<ul>
  <li>
    <b>param-replace.py:</b>
    <ul>
      <li>Why: Mass find/replace of all parameters in a URL with a given payload.</li>
      <li>Uses: Open Redirect, SSRF</li>
      <li>Syntax: <code>python3 param-replace.py --infile [file with ton of URLs in it] --outfile [where to save the results] --payload [a malicious callback link (burp collab>)]</code></li>
    </ul>
  </li>
  <li>
    <b>param-stuffing.py:</b>
    <ul>
      <li>Why: Stuff given parameters in a URL with a given payload.</li>
      <li>Uses: Open Redirect, SSRF</li>
      <li>Syntax: <code>python3 param-stuffing.py --infile [file with ton of URLs in it] --outfile [where to save the results] --params [url redirect u r etc]  --payload [a malicious callback link (burp collab>)]</code></li>
    </ul>
  </li>
</ul>
</details>
