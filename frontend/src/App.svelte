<script>
    import { HtmlTagHydration } from "svelte/internal";


  const videoModules = import.meta.glob("../../content/*.mp4");

  let videoPaths = [];

  for (const modulePath in videoModules) {
    videoModules[modulePath]().then(({ default: imageUrl }) => {
      videoPaths.push(imageUrl);
      videoPaths.sort(() => (Math.random() > .5) ? 1 : -1);

      videoPaths = videoPaths;
    });
  }

  const imageModulesPNG = import.meta.glob("../../content/*.png");
  const imageModulesJPG = import.meta.glob("../../content/*.jpg");

  let imagePaths = [];  

  for (const modulePath in imageModulesPNG) {
    imageModulesPNG[modulePath]().then(({ default: imageUrl }) => {
      imagePaths.push(imageUrl);
      imagePaths.sort(() => (Math.random() > .5) ? 1 : -1);

      
      imagePaths = imagePaths;
    });
  }

  console.log(imagePaths);
  for (const modulePath in imageModulesJPG) {
    imageModulesJPG[modulePath]().then(({ default: imageUrl }) => {
      imagePaths.push(imageUrl);
      imagePaths.sort(() => (Math.random() > .5) ? 1 : -1);
      imagePaths = imagePaths;
    });
  }



</script>

<body>
  <div class="gridbox">
    {#each videoPaths as gg}
      <video src="{gg}" class="image" type="video/mp4" playsinline muted autoplay loop/>
    {/each}

    {#each imagePaths as hh}
      <img src="{hh}" class="image"/>
    {/each}
  </div>
</body>

<style>

  body {
    /* height: 100%; */
    /* overflow: hidden */
  }

 .gridbox{
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  flex-basis: auto;
  /* justify-content: left; */
  align-items: flex-start;
  align-content: flex-start;

  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;


 }
 .image{
  justify-content: left;
  align-items: left;
  object-fit: contain;
  height: 150px;
  margin: 0px;
  padding: 0px;

 }

 .image{
  justify-content: left;
  align-items: left;
  object-fit: contain;
  height: 150px;
  margin: 0px;
  padding: 0px;

 }

 
</style>
