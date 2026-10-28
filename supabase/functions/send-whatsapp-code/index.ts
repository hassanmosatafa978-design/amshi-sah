Deno.serve(async (req) => {
  try {
    const { phone, code } = await req.json();

    if (!phone || !code) {
      return new Response(
        JSON.stringify({ error: "phone و code مطلوبان" }),
        {
          status: 400,
          headers: { "Content-Type": "application/json" }
        }
      );
    }

    // هنا سنضع اتصال WhatsApp Business API
    // بعد اختيار مزود الخدمة.

    return new Response(
      JSON.stringify({
        ok: true,
        message: "تم تجهيز طلب إرسال الكود"
      }),
      {
        status: 200,
        headers: { "Content-Type": "application/json" }
      }
    );

  } catch (error) {
    return new Response(
      JSON.stringify({
        error: "حدث خطأ في الطلب"
      }),
      {
        status: 500,
        headers: { "Content-Type": "application/json" }
      }
    );
  }
});
