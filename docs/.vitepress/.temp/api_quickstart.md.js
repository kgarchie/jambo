import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Quickstart","description":"","frontmatter":{},"headers":[],"relativePath":"api/quickstart.md","filePath":"api/quickstart.md"}');
const _sfc_main = { name: "api/quickstart.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="quickstart" tabindex="-1">Quickstart <a class="header-anchor" href="#quickstart" aria-label="Permalink to &quot;Quickstart&quot;">​</a></h1><h2 id="introduction" tabindex="-1">Introduction <a class="header-anchor" href="#introduction" aria-label="Permalink to &quot;Introduction&quot;">​</a></h2><p>Howdy, how&#39;s the weather?</p><p>These docs are also available in the <a href="https://github.com/kgarchie/jambo/tree/main/docs" target="_blank" rel="noreferrer">docs/</a> folder of the project, it&#39;s <a href="https://vitepress.dev/" target="_blank" rel="noreferrer">vitepress</a> powered and can be served locally by using the following command in that directory.</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">pnpm</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> run</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> docs:dev</span></span></code></pre></div><p>This is done automagically when running the server and is accessible via <a href="http://localhost/docs" target="_blank" rel="noreferrer">http://localhost/docs</a> or <a href="http://localhost:5173/jambo" target="_blank" rel="noreferrer">http://localhost:5173/jambo</a>. You may as well just skim the raw markdown files in the <a href="https://github.com/kgarchie/jambo/tree/main/docs" target="_blank" rel="noreferrer">docs/</a> folder should you wish to.</p><p>Here&#39;s the PostMan collection: <a href="https://god.gw.postman.com/run-collection/15264165-ff91f75b-81bb-4bda-b45e-24002ddad076?action=collection%2Ffork&amp;source=rip_markdown&amp;collection-url=entityId%3D15264165-ff91f75b-81bb-4bda-b45e-24002ddad076%26entityType%3Dcollection%26workspaceId%3D91d100e3-340c-4dbd-b05b-e5eabbc100e7" target="_blank" rel="noreferrer"><img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="${ssrRenderStyle({ "width": "128px", "height": "32px" })}"></a></p><h2 id="installation" tabindex="-1">Installation <a class="header-anchor" href="#installation" aria-label="Permalink to &quot;Installation&quot;">​</a></h2><p>You can install this project in two ways, either via Docker or via Shell Scripting.</p><h3 id="docker-recommended" tabindex="-1">Docker (Recommended) <a class="header-anchor" href="#docker-recommended" aria-label="Permalink to &quot;Docker (Recommended)&quot;">​</a></h3><p>I have provided a <a href="./docker-compose.yml">Docker Compose</a> for the easiest deployment.</p><h4 id="prerequisites" tabindex="-1">Prerequisites <a class="header-anchor" href="#prerequisites" aria-label="Permalink to &quot;Prerequisites&quot;">​</a></h4><ul><li><a href="https://docs.docker.com/get-docker/" target="_blank" rel="noreferrer">Docker</a> - You need docker installed.</li></ul><p>Then run the following command in the root directory of the project.</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">docker-compose</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> up</span></span></code></pre></div><p>This will spin up all the needed containers and the default django-rest-framework API is accessible via <a href="http://localhost" target="_blank" rel="noreferrer">http://localhost</a>:{port}/api/. The port is determined whether it&#39;s in docker or not.</p><h3 id="shell-scripting" tabindex="-1">Shell Scripting <a class="header-anchor" href="#shell-scripting" aria-label="Permalink to &quot;Shell Scripting&quot;">​</a></h3><p>I have also provided a <a href="https://github.com/kgarchie/jambo/tree/main/docs" target="_blank" rel="noreferrer">shell script</a> for easy non-docker deployment. This time however, you need to have the following installed:</p><h3 id="prerequisites-1" tabindex="-1">Prerequisites <a class="header-anchor" href="#prerequisites-1" aria-label="Permalink to &quot;Prerequisites&quot;">​</a></h3><ul><li><a href="https://www.python.org/downloads/" target="_blank" rel="noreferrer">Python 3</a> - You need at least python 3.10 installed. Due to the use of type hints</li><li><a href="https://nodejs.org/en/download/" target="_blank" rel="noreferrer">Node</a> - You need node installed. This is for the documentation.</li><li><a href="https://www.postgresql.org/download/" target="_blank" rel="noreferrer">Postgres</a> - You need postgres installed. Make sure there exists a database whose URI string should be added to the <code>.env</code>.</li><li><a href="https://redis.io/download" target="_blank" rel="noreferrer">Redis</a> - Optional, could be run as a container, wsl or vm</li><li>Nginx is not implemented outside docker due to known issues - Skip</li></ul><p>Then run the following command in the root directory of the project.</p><h5 id="linux" tabindex="-1">Linux <a class="header-anchor" href="#linux" aria-label="Permalink to &quot;Linux&quot;">​</a></h5><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">chmod</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> +x</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> run.sh</span><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}"> &amp;&amp; </span><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">./run.sh</span></span></code></pre></div><h5 id="windows" tabindex="-1">Windows <a class="header-anchor" href="#windows" aria-label="Permalink to &quot;Windows&quot;">​</a></h5><div class="language-shell vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">shell</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">./run.bat</span></span></code></pre></div><div class="info custom-block"><p class="custom-block-title">INFO</p><p>You may run into an Execution-Policy error on Windows, in that case, you need to execute the following command in an admin window before retrying the step above in a fresh window again. See <a href="https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4#:~:text=Copy-,Set%2DExecutionPolicy%20%2DExecutionPolicy%20RemoteSigned%20%2DScope%20LocalMachine,-Get%2DExecutionPolicy%20%2DList" target="_blank" rel="noreferrer">this</a></p></div><div class="language-shell vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">shell</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">Set-ExecutionPolicy</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> RemoteSigned</span></span></code></pre></div><h2 id="secrets" tabindex="-1">Secrets <a class="header-anchor" href="#secrets" aria-label="Permalink to &quot;Secrets&quot;">​</a></h2><p>Environment variables should be stored in a <code>.env</code> file in the root directory of the project. You can rename the <code>.env.example</code> file to <code>.env</code> and fill in the necessary details. It&#39;s rudimentary and self-documented with comments.</p><p>You will notice that if the app will create a <code>SECRET_KEY</code> for you and store it in the <code>.env</code> file if you don&#39;t provide one. This is not recommended for production, so always define a <code>SECRET_KEY</code> in your <code>.env</code> file or environment. The <code>SECRET_KEY</code> is used for hashing and encryption. It&#39;s just a long random string, can be anything.</p><h2 id="testing" tabindex="-1">Testing <a class="header-anchor" href="#testing" aria-label="Permalink to &quot;Testing&quot;">​</a></h2><p>I have included tests to ensure the API is working as expected. Running tests can be done via the following command once the server is up</p><div class="language-shell vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">shell</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#6F42C1", "--shiki-dark": "#B392F0" })}">python</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> manage.py</span><span style="${ssrRenderStyle({ "--shiki-light": "#032F62", "--shiki-dark": "#9ECBFF" })}"> test</span></span></code></pre></div><div class="info custom-block"><p class="custom-block-title">INFO</p><p>I used Faker for data generation, so there is a non-zero chance that some primary keys may clash. If this happens, just run the tests again.</p></div><div class="warning custom-block"><p class="custom-block-title">WARNING</p><p>You need Redis running for the tests to pass.</p></div><div class="danger custom-block"><p class="custom-block-title">DANGER</p><p>Do not use Pycharm&#39;s built in test runner or debugger as it won&#39;t initialise settings and environment variable therein properly</p></div></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("api/quickstart.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const quickstart = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  quickstart as default
};