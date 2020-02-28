Various tools I've made for bug bounty hunting

<details>
<summary>/js</summary>
<ul>
  <li>beautify-js.py: python3 beautify-js.py --infile [file with a ton of URLS in it] --outdir [where to save the beautified results]</li>
</ul>
</details>

<details>
<summary>/ssrf</summary>
<ul>
  <li>sentry-scraping-ssrf.py: python3 sentry-scraping-ssrf.py --infile [file with a ton of URLS in it] --payload [a malicious callback link (burp collab?) --threads [x]</li>
</ul>
</details>

<details>
<summary>/generators</summary>
<ul>
  <li>wayback-words.py: python3 wayback-words.py --infile [file with a ton of URLs in it] --outfile [where to save the generated list] --exclusions [extensions to exclude (ie: .png .jpg)]</li>
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
</ul>
