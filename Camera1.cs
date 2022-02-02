using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera1 : MonoBehaviour
{
    IEnumerator RecordFrame()
    {
        yield return new WaitForEndOfFrame();
        var texture = ScreenCapture.CaptureScreenshotAsTexture();
        Texture2D tex2D = (Texture2D)texture;
        byte[] bytes = texture.EncodeToPNG();

        System.IO.File.WriteAllBytes("/home/mpcr/Desktop/DataSet_SLAM/Image_" + Random.Range(0, 100000) + ".png", bytes);

        // cleanup
        Object.Destroy(texture);
    }

    public void LateUpdate()
    {
        StartCoroutine(RecordFrame());
    }
}
