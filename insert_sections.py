import re

with open('index.html', 'r') as f:
    content = f.read()

new_sections = """
    <!-- 4. PRODUCT COLLECTION -->
    <section>
      <div class="section-title-wrapper" style="flex-direction: column; align-items: flex-start; gap: 8px;">
        <div class="badge" style="margin: 0; background: transparent; border: none; padding: 0; color: #888;">RUDY PROJECT UTMB COLLECTION</div>
        <h2 class="section-title" style="font-size: clamp(2rem, 4vw, 3.5rem);">PERFORMA DIMULAI DARI SINI</h2>
      </div>
      
      <div class="bento-grid-3">
        <!-- Product 1 -->
        <div class="bento-card p-0 hover-scale" style="background: white; color: black;">
          <img src="assets/WhatsApp Image 2026-05-11 at 14.17.19.jpeg" alt="UTMB Series" style="width: 100%; height: 300px; object-fit: cover;">
          <div style="padding: 24px; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: white; position: absolute; bottom: 0; width: 100%;">
            <h3 style="font-size: 1.2rem; font-weight: 800; font-family: 'Barlow';">UTMB SERIES</h3>
            <p style="font-size: 0.8rem; opacity: 0.8;">Trail Performance Eyewear</p>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="bento-card p-0 hover-scale" style="background: white; color: black;">
          <img src="assets/WhatsApp Image 2026-05-11 at 14.18.05.jpeg" alt="Astral X Desert Matte" style="width: 100%; height: 300px; object-fit: cover;">
          <div style="padding: 24px; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: white; position: absolute; bottom: 0; width: 100%;">
            <h3 style="font-size: 1.2rem; font-weight: 800; font-family: 'Barlow';">ASTRAL X DESERT MATTE</h3>
            <p style="font-size: 0.8rem; opacity: 0.8;">Advanced Photochromic Technology</p>
          </div>
        </div>
        
        <!-- Product 3 -->
        <div class="bento-card p-0 hover-scale" style="background: white; color: black;">
          <img src="assets/WhatsApp Image 2026-05-11 at 14.18.44.jpeg" alt="Designed in Italy" style="width: 100%; height: 300px; object-fit: cover;">
          <div style="padding: 24px; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: white; position: absolute; bottom: 0; width: 100%;">
            <h3 style="font-size: 1.2rem; font-weight: 800; font-family: 'Barlow';">DESIGNED IN ITALY</h3>
            <p style="font-size: 0.8rem; opacity: 0.8;">Premium Aerospace Materials</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. RUNDOWN EVENT -->
    <section>
      <h2 class="section-title" style="text-align: center; width: 100%; max-width: 100%; margin-bottom: 40px; font-size: clamp(2rem, 4vw, 3rem);">RUNDOWN EVENT</h2>
      
      <div style="display: flex; flex-direction: column; gap: 16px; max-width: 800px; margin: 0 auto;">
        
        <div class="bento-card" style="padding: 24px;">
          <div style="color: var(--primary); font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;">08.00 - 17.00</div>
          <h3 style="font-size: 1.2rem; margin-bottom: 8px;">PENGAMBILAN RACE PACK</h3>
          <p style="color: var(--text-sub); font-size: 0.9rem;">Race Pack Collection - H-2 hingga H-1 sebelum lomba di lokasi resmi pendaftaran.</p>
        </div>
        
        <div class="bento-card" style="padding: 24px;">
          <div style="color: var(--primary); font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;">04.30 - 05.00</div>
          <h3 style="font-size: 1.2rem; margin-bottom: 8px;">PEMANASAN & DOA PEMBUKA</h3>
          <p style="color: var(--text-sub); font-size: 0.9rem;">Race Day di BSD City. Persiapan mental dan fisik sebelum flag off dilakukan bersama.</p>
        </div>
        
        <div class="bento-card" style="padding: 24px;">
          <div style="color: var(--primary); font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;">05.00</div>
          <h3 style="font-size: 1.2rem; margin-bottom: 8px;">FLAG OFF 21 KM</h3>
          <p style="color: var(--text-sub); font-size: 0.9rem;">Pelepasan pelari Half Marathon dengan Cut Off Time (COT) 4 jam.</p>
        </div>
        
        <div class="bento-card" style="padding: 24px;">
          <div style="color: var(--primary); font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;">05.30</div>
          <h3 style="font-size: 1.2rem; margin-bottom: 8px;">FLAG OFF 10 KM</h3>
          <p style="color: var(--text-sub); font-size: 0.9rem;">Pelepasan pelari kompetitif 10K dengan Cut Off Time (COT) 2 jam.</p>
        </div>
        
      </div>
    </section>

    <!-- 6. PHOTO CONTEST -->
    <section>
      <div style="max-width: 800px; margin: 0 auto;">
        <h2 class="section-title" style="margin-bottom: 24px; font-size: clamp(2.5rem, 5vw, 4rem); max-width: 100%; line-height: 1.1;">
          ARE YOU READY TO BE THE NEXT <br><span style="color: var(--primary);">RPHM FLYER MODEL?</span>
        </h2>
        <p style="color: var(--text-sub); font-size: 1rem; line-height: 1.6; margin-bottom: 40px;">
          Foto terbaik akan dijadikan model untuk Flyer Event Rudy Project Half Marathon 2026. Tunjukkan gaya larimu, kenakan kacamata Rudy Project, dan jadilah inspirasi jutaan pelari!
        </p>
        
        <div class="bento-card" style="padding: 32px; margin-bottom: 24px; border: 1px solid rgba(123, 47, 255, 0.3);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 16px;">
            <h3 style="font-size: 1.2rem; font-weight: 700;">Syarat & Ketentuan</h3>
            <div style="color: var(--primary); font-size: 1.5rem; font-weight: 800; line-height: 1;">&times;</div>
          </div>
          <ul style="color: var(--text-sub); font-size: 0.95rem; line-height: 1.8; padding-left: 20px;">
            <li>Foto pelari dengan kualitas jelas dan menarik</li>
            <li>Wajib menggunakan kacamata Rudy Project / RPJ</li>
            <li>Format portrait & file resolusi tinggi</li>
            <li>Upload di feeds & Story Instagram (akun tidak di-private)</li>
            <li>Tag & mention @rudyprojectid @arrasadventure</li>
            <li>Gunakan hashtag #RPHMModel #PerformanceStartsInYourHead</li>
          </ul>
        </div>
        
        <div class="bento-card" style="padding: 32px; border: 1px solid rgba(123, 47, 255, 0.3);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 16px;">
            <h3 style="font-size: 1.2rem; font-weight: 700;">Pemenang Mendapatkan</h3>
            <div style="color: var(--primary); font-size: 1.5rem; font-weight: 800; line-height: 1;">&times;</div>
          </div>
          <ul style="color: var(--text-sub); font-size: 0.95rem; line-height: 1.8; padding-left: 20px;">
            <li>Rudy Project Eyewear (Eksklusif)</li>
            <li>Smartwatch Premium</li>
          </ul>
        </div>
      </div>
    </section>

"""

content = content.replace("  </main>", new_sections + "\  </main>")

with open('index.html', 'w') as f:
    f.write(content)

print("Inserted new sections")
