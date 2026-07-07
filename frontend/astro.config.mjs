import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://portfolio.pages.dev",
  base: "/",
  output: "static",
  server: {
    port: 4321,
  },
});
