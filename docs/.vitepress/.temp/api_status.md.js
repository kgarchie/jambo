import { ssrRenderAttrs, ssrRenderStyle } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"Status","description":"","frontmatter":{},"headers":[],"relativePath":"api/status.md","filePath":"api/status.md"}');
const _sfc_main = { name: "api/status.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="status" tabindex="-1">Status <a class="header-anchor" href="#status" aria-label="Permalink to &quot;Status&quot;">​</a></h1><h2 id="get-status" tabindex="-1">GET Status <a class="header-anchor" href="#get-status" aria-label="Permalink to &quot;GET Status&quot;">​</a></h2><p>GET /api/status</p><p>Get&#39;s the server status.</p><blockquote><p>Response Examples</p></blockquote><blockquote><p>200 Response</p></blockquote><div class="language-json vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">json</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="${ssrRenderStyle({ "--shiki-light": "#24292E", "--shiki-dark": "#E1E4E8" })}">{}</span></span></code></pre></div><h3 id="responses" tabindex="-1">Responses <a class="header-anchor" href="#responses" aria-label="Permalink to &quot;Responses&quot;">​</a></h3><table><thead><tr><th>HTTP Status Code</th><th>Meaning</th><th>Description</th><th>Data schema</th></tr></thead><tbody><tr><td>200</td><td><a href="https://tools.ietf.org/html/rfc7231#section-6.3.1" target="_blank" rel="noreferrer">OK</a></td><td>Success</td><td>Inline</td></tr></tbody></table></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("api/status.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const status = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  status as default
};
